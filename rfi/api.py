from tastypie.contrib.gis.resources import ModelResource
from tastypie.validation import Validation
from tastypie.constants import ALL
from rfi.models import RequestForImagery
from django.contrib.gis.geos import GEOSGeometry

class RFIResource(ModelResource):
    class Meta:
        resource_name = "rfi"
        queryset = RequestForImagery.objects.all()

        filtering = {
                'polys': ALL,
                }

class RFIValdation(Validation):
    def is_valid(self, bundle, request=None):
        d = bundle.data.items()
        errors = {}

        #Must have a contact name
        if d['requestor_name'] is None:
            errors['requestor_name'] = ['NAME REQUIRED']
            return errors
        #Must have a valid bbox
        polywkt = d['bounds']
        if polywkt is None:
            errors['bounds'] = ['REQUEST BOUNDS REQUIRED']
            return errors
        poly = GEOSGeometry(polywkt)

        if poly.geom_typeid != 3:
            errors['bounds'] = ['REQUEST BOUNDS NOT A POLYGON']
            return errors
        (xmin, ymin, xmax, ymax) = poly.extent
        if not ymin > -90 and \
                ymax < 90 and \
                xmin > -180 and \
                xmax < 180:
            return {'bounds': 'INVALID BOUNDS'}

