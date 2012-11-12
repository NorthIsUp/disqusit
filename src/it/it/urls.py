from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'disqusit.views.home', name='home'),
    # url(r'^disqusit/', include('disqusit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}, 'index'),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('django.contrib.auth.urls')),
)

