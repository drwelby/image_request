from rfi.models import RequestForImagery, TestArea
from django.contrib.gis import admin

admin.site.register(RequestForImagery, admin.GeoModelAdmin)
admin.site.register(TestArea, admin.GeoModelAdmin)

