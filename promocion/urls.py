from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'views.main_page'),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'views.logout_page'),

    # CRM
    url(r'^crm/', include('crm.urls')),

    # Prospectos
    url(r'^prospectos/', include('prospectos.urls')),


    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),

    url(r'^admin/', include(admin.site.urls)),
)
