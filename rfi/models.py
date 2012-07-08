from django.contrib.gis.db import models
from django.db.models import signals
import requests
from requests.auth import HTTPBasicAuth

from local_settings import GEOSERVER_USER, GEOSERVER_PASSWORD
from local_settings import GEOSERVER_BASE_URL,WORKSPACE,DATASTORE,FEATURE

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

    need_by_date = models.DateTimeField(blank=True)

    PRIORITIES = (
            ('high', 'High'),
            ('routine', 'Routine'),
            ('low', 'Low'),
            )
    priority = models.CharField(max_length=10, choices=PRIORITIES, blank=True)

    nextview_ack = models.BooleanField(blank=True)

    objects = models.GeoManager()

def updateboundshandler(sender=None, **kwargs):

    if sender is RequestForImagery:
        updatebounds()

def updatebounds(sender=None, **kwargs):
    # construct url from local_settings.py
    # later we'll also configure geoserver through REST
    #
    # curl -u admin:geoserver -i -XPUT -H 'Content-type: text/xml'
    # -d '<featureType><name>rfi_requestforimagery</name><projectionPolicy>FORCE_DECLARED</projectionPolicy></featureType>'
    # http://192.168.244.151:8080/geoserver/rest/workspaces/rfi/datastores/rfi/featuretypes/rfi_requestforimagery.xml

    #payload = {'recalculate':'nativebbox,latlonbbox'}

    url = "%s/geoserver/rest/workspaces/%s/datastores/%s/featuretypes/%s.xml" % (GEOSERVER_BASE_URL,WORKSPACE,DATASTORE,FEATURE)

    files = {'file': ('rfi_requestforimagery.xml', '<featureType><name>rfi_requestforimagery</name><projectionPolicy>FORCE_DECLARED</projectionPolicy></featureType>')}
    
    headers = {'Content-type': 'text/xml'}
    
    print url

    #PUT the request
    r = requests.put(url, files=files, headers=headers, auth=HTTPBasicAuth(GEOSERVER_USER, GEOSERVER_PASSWORD))
    # handle the response
    r.raise_for_status()

#signals.post_save.connect(updateboundshandler)
#signals.post_delete.connect(updateboundshandler)
