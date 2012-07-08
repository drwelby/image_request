from django.conf.urls.defaults import *

from rfi.api import RFIResource

entry_resource = RFIResource()

urlpatterns = patterns('',
        (r'^api/', include(entry_resource.urls)),
        )
