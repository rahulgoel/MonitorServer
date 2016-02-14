from django.conf.urls import patterns, include, url
from django.contrib import admin
from manager import MonitorServices
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monitorHardware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                url(r'^query/', MonitorServices.getAtTime),
    url(r'^querytime/', MonitorServices.getAtTime),
)


