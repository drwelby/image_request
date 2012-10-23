from tastypie.validation import Validation
from django.contrib.gis.geos import GEOSGeometry
from urllib2 import urlopen
from rfi.tools import getpoly
import json


class RFIValidation(Validation):
    def is_valid(self, bundle, request=None):
        d = bundle.data
        errors = {}

        #Must have a contact name
        if 'requestor_name' not in d:
            errors['requestor_name'] = ['NAME REQUIRED']
            return errors
        if d['requestor_name'] is None:
            errors['requestor_name'] = ['NAME REQUIRED']
            return errors
        #Must have a valid bbox
        if 'bounds' not in d:
            errors['bounds'] = ['REQUEST BOUNDS REQUIRED']
            return errors 
        if d['bounds'] is None:
            errors['bounds'] = ['REQUEST BOUNDS REQUIRED']
            return errors 
        polyjson = json.dumps(d['bounds'])
        try:
            print type(d['bounds'])
            poly = GEOSGeometry(polyjson)
        except:
            errors['bounds'] = ['INVALID GEOMETRY']
            return errors 
        if poly.geom_typeid != 3:
            errors['bounds'] = ['REQUEST BOUNDS NOT A POLYGON']
            return errors 
        (xmin, ymin, xmax, ymax) = poly.extent
        if ymin < -90 or \
                ymax > 90 or \
                xmin < -180 or \
                xmax > 180:
            errors['bounds'] = ['INVALID BOUNDS']
        return errors 

