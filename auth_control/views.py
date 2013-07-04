# Django Requriments
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.template import RequestContext # for POST
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.conf import settings

from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Developer Requirements
from django.utils import simplejson


#########################################################################
# Page: < Any Page (base_home) - Login >
# 
# Requests: < auth_log_in(request) >
#
#   Description:
#       this request is called when usr wants to log in. we will see if 
#       their 
#
#########################################################################
@csrf_protect
@csrf_exempt
def auth_log_in(request):
    status = "success"
    """
    if request.method == 'POST':
        if request.POST:
            word = word.replace('_', ' ') 
            # retrieve author's name and list name
            modified = request.POST['modified']
            author = request.POST['author_name']
            list_name = request.POST['list_name']
            manager = Term_Manager(list_name)
            if not manager.store_vocabulary_definition_given_vocabulary_and_vocabulary_list(author, word, modified):
                status = "fail"
    """
    
    return render_to_response(
        'auth_control/login.html',
        {
        }
    )


