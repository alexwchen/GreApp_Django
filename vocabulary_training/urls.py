from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('vocabulary_training.views',
    
    # Display All The List We Have
    url(r'^home/$', 'display_all_vocabulary_lists'),

    # Display A Single List User Selected
    url(r'^(?P<list_title>\w+)/(?P<list_author>\w+)/(?P<list_id>\w+)$', 'display_single_list'),

    # GET & POST in Study Section
    url(r'^retrive_word_info/(?P<word>\w+)/$', 'retrive_word_info'),
    url(r'^store_word_info/(?P<word>\w+)/$', 'store_word_info'),
    url(r'^store_word_input_box/(?P<word>\w+)/$', 'store_word_input_box'),
    url(r'^store_word_definition/(?P<word>\w+)/$', 'store_word_definition'),
    url(r'^store_word_name/(?P<word>\w+)/$', 'store_word_name'),
    url(r'^delete_vocabulary_word_from_list/(?P<word>\w+)/$', 'delete_vocabulary_word_from_list'),
    

    # GET & POST in Training Section
    url(r'^get_next_list_of_question/$', 'training_question_mode'),

    # GET & POST in Test Section
    url(r'^get_test_question_given_amount/$', 'test_question_mode'),
    
    # not revelent - debug use
    url(r'^meta/$', 'display_meta'),
)

