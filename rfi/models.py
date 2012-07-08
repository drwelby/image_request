from django.contrib.gis.db import models
from django.db.models import signals
import requests
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

def updatebounds():
    # construct url from local_settings.py
    # later we'll just configure geoserver through REST
    #
    payload = {'recalculate':'nativebbox,latlonbbox'}
    url = "%s/workspaces/%s/datastores/%s/featuretypes/%s" % (WORKSPACE,DATASTORE,FEATURE)

    #PUT the request
    r = requests.put(url, params=payload)
    # handle the response
    r.raise_for_status()

signals.post_save.connect(updatebounds)
