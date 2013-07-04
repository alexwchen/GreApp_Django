from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('auth_control.views',
    
    # Authorization for login, logout
    url(r'^login/$', 'auth_log_in'),

)

