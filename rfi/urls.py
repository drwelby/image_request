from django.conf.urls.defaults import *

from rfi.api import RFIResource

entry_resource = RFIResource()

urlpatterns = patterns('',
        (r'^api/', include(entry_resource.urls)),
        (r'^request/(\d+)/$', 'rfi.views.request_info'),
        (r'^info/(\d+)/$', 'rfi.views.info_window'),
        (r'^new/$', 'rfi.views.new_request'),
        (r'^complete/$', 'rfi.views.complete'),
        )
