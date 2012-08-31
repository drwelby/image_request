from django.contrib.gis.db import models
from django.db.models import signals
from local_settings import GEOSERVER_USER, GEOSERVER_PASSWORD
from local_settings import GEOSERVER_BASE_URL,WORKSPACE,DATASTORE,FEATURE

import requests
from django.http import HttpResponse
from django.db import connection, transaction

class RequestForImagery(models.Model):
    requestor_name = models.CharField(max_length=50)
    requestor_email = models.EmailField(blank=True)
    requestor_phone = models.CharField(max_length=50, blank=True)

    ORG_CHOICES = (
            ('ngo', 'NGO'),
            ('io', 'IO'),
            ('academic', 'Academic'),
            ('government', 'Government'),
            )
    org_choice = models.CharField(max_length=20, choices=ORG_CHOICES, blank=True)

    supported_operation = models.TextField(blank=True)
    supported_partners = models.TextField(blank=True)
    reason_for_use = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    justification = models.TextField(blank=True)
    bounds = models.PolygonField()

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    IMG_FORMATS = (
            ('nitf', 'NITF'),
            ('sid', 'Mr.SID'),
            ('tif', 'GeoTIFF'),
            ('jpg', 'JPG2000'),
            )
    img_format = models.TextField(max_length=5, choices=IMG_FORMATS, blank=True)

    DELIVERY_FORMATS = (
            ('disk', 'Disk'),
            ('ftp', 'FTP'),
            )
    delivery_format = models.TextField(max_length=5, choices=DELIVERY_FORMATS,blank=True)

    need_by_date = models.DateTimeField(blank=True, null = True)

    PRIORITIES = (
            ('high', 'High'),
            ('routine', 'Routine'),
            ('low', 'Low'),
            )
    priority = models.CharField(max_length=10, choices=PRIORITIES, blank=True)

    nextview_ack = models.BooleanField(blank=True)

    objects = models.GeoManager()

def triggerupdate(request):
    # in case you want to trigger an update from a view as a test
    updateboundshandler(sender=RequestForImagery)
    return HttpResponse ("updated")

def updateboundshandler(sender=None, **kwargs):

    if sender is RequestForImagery:
        # Make sure the datastore has the "Estimated Extends" box unchecked,
        # otherwise you will have to deal with this:
        #
        # https://jira.codehaus.org/browse/GEOS-5233
        # In the event ANALYZE has ever been run on the table,
        # we have to update the statistics first.
        #
        #cursor = connection.cursor();
        #cursor.execute("ANALYZE %s;" % FEATURE)
        #transaction.commit_unless_managed()
        updatebounds()

def updatebounds():
    # construct url from local_settings.py
    # later we'll also configure geoserver through REST
    #
    # curl -u admin:geoserver -i -XPUT -H 'Content-type: text/xml'
    # -d '<featureType><name>rfi_requestforimagery</name><projectionPolicy>FORCE_DECLARED</projectionPolicy></featureType>'
    # http://192.168.244.151:8080/geoserver/rest/workspaces/rfi/datastores/rfi/featuretypes/rfi_requestforimagery.xml

    # GeoServer recalculate bug - delimiter is ' in 2.2 rc1, not ,
    
    url = "%s/geoserver/rest/workspaces/%s/datastores/%s/featuretypes/%s.xml?recalculate=nativebbox'latlonbbox" \
            % (GEOSERVER_BASE_URL,WORKSPACE,DATASTORE,FEATURE)

    data = '''<featureType>
                <name>rfi_requestforimagery</name>
                </featureType>'''
    
    headers = {'Content-type': 'text/xml'}
    
    r = requests.put(url, data=data, headers=headers, auth=(GEOSERVER_USER, GEOSERVER_PASSWORD))
    # handle the response
    try:
        r.raise_for_status()
    except:
        raise Exception("Geoserver error when updating bounds")

# Connect the save and delete signals
# DOESN'T WORK WITH SAVES FROM THE ADMIN!
# Actually, it's probably easier just to set the bounds of the layer to the whole globe
#signals.post_save.connect(updateboundshandler)
#signals.post_delete.connect(updateboundshandler)
