# Django Requriments
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.template import RequestContext # for POST
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.conf import settings
from django.utils import simplejson

from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Developer Requirements
from import_monster import *
from create_manager import *


#########################################################################
# Page: < Create Page >
# 
# Requests: < update_internal_word_database(request) > 
#   Description:
#       this function does various things to modify or update the
#       internal word database. 
#       1.  delete internal database
#       2.  load data from what we crawl
#       3.  fix some quick bug 
#
#   Note:
#
#########################################################################

def update_internal_word_database(request):

    # Delete everything in the database
    # delete_everything_in_internal_database()

    # A quick fix to vocabulary name and definition
    # quick_hack()

    
    # Import all words, 130000 of them, into the database
	load_each_word_file_into_internal_db()
	return render_to_response(
        'create_new_list/create_vocabulary_list.html',
        {
        }
    )


#########################################################################
# Page: < Create Page >
# 
# Requests: < create_vocabulary_list(request) > 
#   Description:
#       initialization of create vocabulary list interface
#
#   Note:
#
#########################################################################
def create_vocabulary_list(request):
    
    default_block_number = range(10)
    return render_to_response(
        'create_new_list/create_vocabulary_list.html',
        {
            'default_block_number':default_block_number,
        }
    )


#########################################################################
# Page: < Create Page - Import Section>
# 
# Requests: < create_vocabulary_list(request) > 
#   Description:
#       This function is called when import button is pressed. It should
#       take the list and parsed it into a json data send it back to the 
#       manual section
#
#   Note:
#
#########################################################################
def import_section_process_pasted_list(request):
    
    status = "success"
    if request.method == 'GET':
        user_pasted_list = request.GET['user_pasted_list']
        splited = user_pasted_list.split('\n')
        term_dict = {}

        for term in splited:
            splited_term = term.split('\t')
            term = splited_term[0]
            term_def = splited_term[1]

            if term not in term_dict.keys():
                term_dict[term] = term_def

        if len(term_dict)!=0:
            json_return = simplejson.dumps(term_dict)
            return HttpResponse(json_return)
        else:
            return HttpResponse('fail')

    return HttpResponse('fail')


#########################################################################
# Page: < Create Page - Manual Section>
# 
# Requests: < create_vocabulary_list(request) > 
#   Description:
#       This function is called when import button is pressed. It should
#       take the list and parsed it into a json data send it back to the 
#       manual section
#
#   Note:
#
#########################################################################
@csrf_protect
@csrf_exempt
def manual_section_user_pasted_list(request):
    
    status = "success"
    if request.method == 'POST':
        if request.POST:
            list_name = request.POST['list_name']
            author_name = request.POST['author_name']
            total = (len(request.POST)-2)/2
            term_def_dictionary = {}
            for idx in range(total):
                term = request.POST['result['+str(idx)+'][term]']
                definition = request.POST['result['+str(idx)+'][definition]']
                term_def_dictionary[term] = definition
            list_id = store_user_pasted_list(list_name, author_name, term_def_dictionary)
            
            return HttpResponse(list_id)
    return HttpResponse('fail')

