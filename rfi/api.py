from tastypie.contrib.gis.resources import ModelResource
from rfi.models import RequestForImagery

class RFIResource(ModelResource):
    class Meta:
        resource_name = "rfi"
        queryset = RequestForImagery.objects.all()

        filtering = {
                'polys': ALL,
                }
