from django.conf.urls.defaults import patterns, include, url
from ga_ows.views.wfs import WFS

from rfi import models as m
#from rfi.models import RequestForImagery

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('image_request.rfi.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

)
