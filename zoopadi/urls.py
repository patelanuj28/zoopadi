from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zoopadi.views.home', name='home'),
    # url(r'^zoopadi/', include('zoopadi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/logout/', 'django.contrib.auth.views.logout',{'next_page': '/admin/'}),

    # Uncomment the next line to enable the admin:
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
