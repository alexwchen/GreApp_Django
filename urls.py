from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout
# local machine settings
from django.views.static import *
from django.conf import settings

urlpatterns = patterns('',
    
    # Home Page
    url(r'^$', 'vocabulary_training.views.display_all_vocabulary_lists'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^.*/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Display Single User List
    url(r'^training/', include('vocabulary_training.urls')),
    (r'^training/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Create
    url(r'^create/', include('create_new_list.urls')),
    (r'^create/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Team
    url(r'^team/$', 'team.views.display_team'),

    # Auth
    url(r'^auth_control/', include('auth_control.urls')),

    # this is for internal testing - debugging use
    url(r'^test/$', 'vocabulary_training.views.display_test'),

    #(r'^create/.*/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #url(r'^$', 'vocabulary_training.views.display_all_vocabulary_list'),
    
    # Admin Page
    url(r'^admin/', include(admin.site.urls)),
)
