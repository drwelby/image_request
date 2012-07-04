from django.contrib.gis.db import models

class RequestForImagery(models.Model):
    requestor_name = models.CharField(max_length=50)
    requestor_email = models.EmailField()
    requestor_phone = models.CharField(max_length=50)

    ORG_CHOICES = (
            ('ngo', 'NGO'),
            ('io', 'IO'),
            ('academic', 'Academic'),
            ('government', 'Government'),
            )
    org_choice = models.CharField(max_length=20, choices=ORG_CHOICES)

    supported_operation = models.TextField()
    supported_partners = models.TextField()
    reason_for_use = models.TextField()
    objective = models.TextField()
    justification = models.TextField()
    bounds = models.PolygonField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    IMG_FORMATS = (
            ('nitf', 'NITF'),
            ('sid', 'Mr.SID'),
            ('tif', 'GeoTIFF'),
            ('jpg', 'JPG2000'),
            )
    img_format = models.TextField(max_length=5, choices=IMG_FORMATS)

    DELIVERY_FORMATS = (
            ('disk', 'Disk'),
            ('ftp', 'FTP'),
            )
    delivery_format = models.TextField(max_length=5, choices=DELIVERY_FORMATS)

    need_by_date = models.DateTimeField()

    PRIORITIES = (
            ('high', 'High'),
            ('routine', 'Routine'),
            ('low', 'Low'),
            )
    priority = models.CharField(max_length=10, choices=PRIORITIES)

    nextview_ack = models.BooleanField()

    objects = models.GeoManager()



