from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('create_new_list.views',
    
    url(r'^$', 'create_vocabulary_list'),
    url(r'^update_internal_word_database/$', 'update_internal_word_database'),
    url(r'^process_pasted_list/$', 'import_section_process_pasted_list'),
    url(r'^save_user_list/$', 'manual_section_user_pasted_list'),
)

