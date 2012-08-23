from tastypie.contrib.gis.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import Validation
from tastypie.constants import ALL
from tastypie import fields
from rfi.models import RequestForImagery, TestArea
from rfi.validation import RFIValidation
from rfi.tools import getpoly
from urllib2 import urlopen
import json


class RFIResource(ModelResource):

    class Meta:
        resource_name = "rfi"
        authorization = Authorization()
        validation = RFIValidation()
        queryset = RequestForImagery.objects.all()

        filtering = {
                'polys': ALL,
                }

    def hydrate_bounds(self, bundle):
        '''bounds can be geojson or uri of external object with geojson bounds'''

        d = bundle.data
        polyjson = json.dumps(d['bounds'])
        if type(polyjson) == str:
            try:
                response = urlopen(d['bounds']).read()
                otherobj = json.loads(response)
            except:
                return bundle
            # find the geojson and swap it out
            polyjson = getpoly(otherobj) 
            # No geojson, send it on
            if not polyjson:
                return bundle
            # we have another object's geometry, we can swap it in the bundle
            bundle.data['bounds'] = polyjson
        return bundle

class TestAreaResource(ModelResource):

    class Meta:
        resource_name = "test"
        authorization = Authorization()
        validation = Validation()
        queryset = TestArea.objects.all()

        filtering = {
                'polys': ALL,
                }
