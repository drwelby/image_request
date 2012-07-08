from rfi.models import RequestForImagery
from django.contrib.gis import admin

admin.site.register(RequestForImagery, admin.GeoModelAdmin)

