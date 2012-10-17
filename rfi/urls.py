from django.conf.urls.defaults import *

from rfi.api import RFIResource, TestAreaResource

rfi_resource = RFIResource()
test_resource = TestAreaResource()

urlpatterns = patterns('',
        (r'^api/', include(rfi_resource.urls)),
        (r'^api/', include(test_resource.urls)),
        (r'^request/(\d+)/$', 'rfi.views.request_info'),
        (r'^info/(\d+)/$', 'rfi.views.info_window'),
        (r'^edit/(\d+)/$', 'rfi.views.edit_request'),
        (r'^new/$', 'rfi.views.new_request'),
        (r'^complete/$', 'rfi.views.complete'),
        )
