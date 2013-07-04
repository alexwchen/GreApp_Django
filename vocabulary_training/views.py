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
from terms import Term
from terms import parse_to_terms_and_def 
from term_manager import Term_Manager
from quizbot import Quizbot

import datetime  
import random
from django.utils import simplejson



#########################################################################
# Page: < Home Page >
# 
# Requests: < display_all_vocabulary_lists(request) > 
#   Description:
#       display_all_vocabulary_lists is used in the home page. It will 
#       display all the vocabulary list we have in the system.
#
#   Note:
#       this request still need tunning in the future when we add user
#       log in function
#
#########################################################################

def display_all_vocabulary_lists(request):

    if request.user.is_authenticated():
        print 'User Authenticated'
    else:
        print 'User Not Authenticated'

    manager = Term_Manager('geting_all_list')
    lists =  manager.get_all_vocabulary_lists().order_by('title')
    return render_to_response(
        'vocabulary_training/display_all_vocabulary_lists.html',
        {
            'lists':lists,
        }
    )

#########################################################################
# Page: < Main List Page >
#       < Including Study Page, Training Page, Test Page >
# 
# Requests: < display_single_list(request, list_title) > 
#   Description:
#       this request prepare initial data needed for the Study Page,
#       Trainig Page and Test Page. 
#
#   Note:
#       this request still need tunning in the future when we add user
#       log in function. Author is fixed to me now. Need to look into it 
#       later
#
#########################################################################
def display_single_list(request, list_title, list_author, list_id):
    
    # preparing information for "Study Section"
    manager = Term_Manager(list_title.replace('_',' '))    
    term_list = manager.get_term_obj_list_from_database(list_id)

    # preparing information for "Training Section"
    Qbot = Quizbot(list_title.replace('_', ' '), list_author.replace('_',' '))
    OP = Qbot.get_a_list_of_questions_given_amount_and_type(int(len(term_list)/2),'extra_definition')

    # preparing information for "Test Section"
    Test = Qbot.get_a_list_of_questions_given_amount_and_type(10, "mix")
    
    return render_to_response(
        'vocabulary_training/display_single_list.html',
        {
            'title':list_title.replace('_',' '),
            'terms':term_list,
            'author':list_author.replace('_',' '),
            'train_quiz':OP,
            'test_question': Test,
        }
    )

#########################################################################
# Page: < Study Page >
# 
# Requests: < retrive_word_info(request, word) >
#   Description:
#       this request is called in study page when user click on "More".
#       It will get 3 synonym, 3 example sentence, 3 extra definitions
#       for user to select which one is useful to them.
#
#   Note:
#       maybe we wnat more error checking later, and maybe should auto 
#       crawl or crawling option if word is not find in your_dictionary.com
#       this idea will be another request
#
#########################################################################
def retrive_word_info(request, word):
    
    get_term = Term(word)

    examples = get_term.get_all_example_sentences_given_word()
    example_list = []
    for example in examples:
        example = str(example).replace('\n', ' ')
        example_list.append(str(example))
    random.shuffle(example_list)

    synonyms = get_term.get_all_synonyms_given_word()
    syn_list = []
    for syn in synonyms:
        syn_list.append(str(syn))
    random.shuffle(syn_list)

    extra_defs = get_term.get_all_extra_definition_given_word()
    extra_def_list = []
    for extra_def in extra_defs:
        extra_def_list.append(str(extra_def))
    random.shuffle(extra_def_list)


    j_dict = {}
    if len(example_list) > 3:
        j_dict['example'] = example_list[:3]
        j_dict['example_idx'] = 3
    else:
        j_dict['example'] = example_list
        j_dict['example_idx'] = len(example_list)
    
    if len(syn_list) > 3:
        j_dict['synonym'] = syn_list[:3]
        j_dict['synonym_idx'] = 3
    else:
        j_dict['synonym'] = syn_list
        j_dict['synonym_idx'] = len(syn_list)

    if len(extra_def_list) > 3:
        j_dict['extra_def'] = extra_def_list[:3]
        j_dict['extra_def_idx'] = 3
    else:
        j_dict['extra_def'] = extra_def_list
        j_dict['extra_def_idx'] = len(extra_def_list)
    
    json_return = simplejson.dumps(j_dict)
    return HttpResponse(json_return)

#########################################################################
# Page: < Study Page >
# 
# Requests: < store_word_info(request,word) >
#   Description:
#       this request is called in study page when user click on "Save".
#       It stores user's choice of useful additional information back into
#       the database.
#
#   Note:
#
#########################################################################
@csrf_protect
@csrf_exempt
def store_word_info(request,word):

    if request.method == 'POST':
        if request.POST:
            word = word.replace('_', ' ').lower()
            print '------------------'
            print word
            print '------------------'
            # retrieve author's name and list name
            author = request.POST['author_name']
            list_name = request.POST['list_name']
            
            # total number of the extra info user selected
            total = (len(request.POST.keys())-2)/2
            status = "success"
            
            # clean up vocabulary list info, and recreate it
            manager = Term_Manager(list_name)
            if not manager.delete_vocabulary_and_recreate_given_word(author, word):
                status = "fail"
                print 'fuck fail 1'

            # loop through all of them and store them into according lsit
            for count in range(total):
                label = request.POST['result['+ str(count) +'][label]']
                content = request.POST['result['+ str(count) +'][data]']
                label = label.split('_')[-1]
                print label
                print content

                if label == 'definition':
                    if not manager.store_extra_definition_in_user_vocabulary_list(author, word, content):
                        status = "fail"
                elif label == 'synonym':
                    if not manager.store_vocabulary_synonyms_in_user_vocabulary_list(author, word, content):
                        status = "fail"
                elif label == 'example':
                    if not manager.store_vocabulary_example_sentence_in_user_vocabulary_list(author, word, content):
                        status = "fail"

    return HttpResponse(status)


#########################################################################
# Page: < Study Page >
# 
# Requests: < store_word_input_box(request,word) >
#   Description:
#       this request gets called when user modify the additional information
#       they choosed, it will take in the unmodified info, and the mofified 
#       info. It will search for the [extra_definition | example_sentence | 
#       synonym ] based on the unmodified info, and save the modified one.
#
#   Note:
#
#########################################################################
@csrf_protect
@csrf_exempt
def store_word_input_box(request,word):
    status = "success"
    if request.method == 'POST':
        if request.POST:
            word = word.replace('_', ' ') 
            # retrieve author's name and list name
            original = request.POST['original']
            modified = request.POST['modified']
            author = request.POST['author_name']
            list_name = request.POST['list_name']
            category= request.POST['category']
            manager = Term_Manager(list_name)
            if not manager.store_additional_information_given_vocabulary_and_vocabulary_list(author, word, original, modified, category):
                status = "fail"

    return HttpResponse(status)

#########################################################################
# Page: < Study Page >
# 
# Requests: < store_word_name(request,word) >
#   Description:
#      this request is called when usre try to modify term name
#
#   Note:
#      this request is not really working, if we somehow modify the 
#      term to more than one word, it will just fail. This need to be 
#      redo.
#########################################################################
@csrf_protect
@csrf_exempt
def store_word_name(request,word):
    status = "success"
    if request.method == 'POST':
        if request.POST:
            word = word.replace('_', ' ') 
            # retrieve author's name and list name
            modified = request.POST['modified']
            author = request.POST['author_name']
            list_name = request.POST['list_name']
            manager = Term_Manager(list_name)
            if not manager.store_vocabulary_name_given_vocabulary_and_vocabulary_list(author, word, modified):
                status = "fail"
    return HttpResponse(status)

#########################################################################
# Page: < Study Page >
# 
# Requests: < store_word_definition(request,word) >
#
#   Description:
#      this request is called when usre try to modify term definition
#
#########################################################################
@csrf_protect
@csrf_exempt
def store_word_definition(request,word):
    status = "success"
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
    return HttpResponse(status)


#########################################################################
# Page: < Study Page >
# 
# Requests: < delete_vocabulary_word_from_list(request,word) >
#
#   Description:
#       when this function is called, it will delete the word from the list
#       and all revelent information.
#
#########################################################################
@csrf_protect
@csrf_exempt
def delete_vocabulary_word_from_list(request,word):
    status = "success"
    if request.method == 'POST':
        if request.POST:
            word = word.replace('_', ' ') 
            # retrieve author's name and list name
            author = request.POST['author_name']
            list_name = request.POST['list_name']
            manager = Term_Manager(list_name)
            if not manager.delete_vocabulary_recreate_given_word(author, word):
                status = "fail"
    return HttpResponse(status)

#########################################################################
# Page: < Training Page >
# 
# Requests: < training_definition_question_mode(request) >
#
#   Description:
#       this request is called on the training page when the "Next" Button
#       is triggered. It will retrieve 10 new questions. So the user can 
#       answer questions without being interupted.
#   
#
#########################################################################
def training_question_mode(request):
    status = "success"
    if request.method == 'GET':
        author = request.GET['author_name']
        list_name = request.GET['list_name']
        category = request.GET['category']
        # call the right question generator 
        Qbot = Quizbot(list_name, author)
        OP = {}
        if category == "Definition":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "definition")
            print category 
        elif category == "Extra Definition":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "extra_definition")
            print category 
        elif category == "Synonym":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "synonym")
            print category 
        elif category == "Example Sentence":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "example_sentence")
            print category 
        elif category == "Mix":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "mix")
            print category 
        else:
            pass
        # check for error, if nothing is generated
        if len(OP)!=0:
            json_return = simplejson.dumps(OP)
            return HttpResponse(json_return)
        else:
            return HttpResponse('fail')



#########################################################################
# Page: < Training Page >
# 
# Requests: < test_question_mode(request) >
#
#   Description:
#       This request is called by the "Generate" button in the configuration
#       box. It will return the amount of questions requested for exam
#   
#########################################################################
def test_question_mode(request):
    status = "success"
    if request.method == 'GET':
        author = request.GET['author_name']
        list_name = request.GET['list_name']
        category = request.GET['category']
        amount = request.GET['amount']
        
        # call the right question generator 
        Qbot = Quizbot(list_name, author)
        OP = {}
        if category == "Definition":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(int(amount), "definition")
            print category 
        elif category == "Extra Definition":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(int(amount), "extra_definition")
            print category 
        elif category == "Synonym":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(int(amount), "synonym")
            print category 
        elif category == "Example Sentence":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(int(amount), "example_sentence")
            print category 
        elif category == "Mix":
            OP = Qbot.get_a_list_of_questions_given_amount_and_type(10, "mix")
            print category 
        else:
            pass
        # check for error, if nothing is generated
        if len(OP)!=0:
            json_return = simplejson.dumps(OP)
            return HttpResponse(json_return)
        else:
            return HttpResponse('fail')

####################################
#	Purpose:
#       Display all meta info. Useful for debugging.
#
###################################	
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def display_test(request):
    
    return render_to_response(
        'vocabulary_training/test_home.html',
        {
        }
    )
