from tastypie.contrib.gis.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from tastypie import fields
from rfi.models import RequestForImagery
from rfi.validation import RFIValidation

from tastypie.validation import Validation

class RFIResource(ModelResource):

    class Meta:
        resource_name = "rfi"
        authorization = Authorization()
        validation = RFIValidation()
        #validation = Validation()
        queryset = RequestForImagery.objects.all()

        filtering = {
                'polys': ALL,
                }
