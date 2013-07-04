#########################################################################
# File Name: create_manager.py
# Author: Alexander Chen   
#
# Description:
#   create_manager are designed to interface with the database when someone
#   store their list
#
#
# Functions:
#
#########################################################################
from vocabulary_training.models import vocabulary_list
from vocabulary_training.models import vocabulary

from vocabulary_training.models import internal_wordbase_vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary_example_sentence
from vocabulary_training.models import internal_wordbase_vocabulary_synonyms
from vocabulary_training.models import internal_wordbase_vocabulary_extra_definition 

import datetime
from terms import Term
import thread

#########################################################################
# Page: < Create Page >
# 
# Requests: < parse_and_store_one_term(new_term) > 
#   Description:
#       This function is meant to called with multi-threading mechanism.
#       It is means to be download data online and store it into internal
#       word database. 
#
#   Note:
#       The existance of the word is already checked before this function 
#       is called. 
#   
#       We need to come back to store words into a text file, for future
#       memory efficient loading on server.
#
#########################################################################
def parse_and_store_one_term(new_term):

    print new_term.word
    print new_term.definition
    i_v = internal_wordbase_vocabulary(
        vocabulary = new_term.word,
        definition = new_term.definition,
    )
    i_v.save()
    word = str(new_term.word)
    examples = new_term.get_example_sentence_online_given_word(word)
    for example in examples:
        new_example = str(example).replace('\n', ' ')
        print new_example
        v_ex = internal_wordbase_vocabulary_example_sentence(
            master_vocabulary = i_v,
            example_sentences = new_term.strip_one_kind_of_html_tag_from_text( 'li',new_example)
        )
        v_ex.save()
     
    synonyms = new_term.get_synonyms_online_given_word(word)
    for syn in synonyms:
        synonym = str(syn)
        print synonym
        v_syn = internal_wordbase_vocabulary_synonyms(
            master_vocabulary = i_v,
            synonyms = synonym,
        )
        v_syn.save()
    
    meanings = new_term.get_extra_meaning_example_online_given_word(word)
    for meaning in meanings:
        defi = str(meaning).replace('\n', ' ') 
        v_defi = internal_wordbase_vocabulary_extra_definition(
            master_vocabulary = i_v,
            extra_def = str(defi),
        )
        v_defi.save()



#########################################################################
# Page: < Create Page >
# 
# Requests: < store_user_pasted_list(list_name, author_name, term_def_dictionary) > 
#   Description:
#       This function is called when the user press 'import' on the create
#       page. The word definition dictionary is passed in, and we will store 
#       them into the 'vocabulary' table in the database. If the word is not 
#       found, we will use multi-threading and call parse_and_store_one_term
#       function.
#
#   Note:
#       We need to control the number of threads so we won't blow up our 
#       memory limit
#
#########################################################################
def store_user_pasted_list(list_name, author_name, term_def_dictionary):
    
    # create vocabulary list
    v_l = vocabulary_list(
        title = list_name,
        authors = author_name,
        creation_date = datetime.datetime.now(),
        terms = len(term_def_dictionary.keys())
    )
    v_l.save()
    
    # create vocabulary and append to the list we append to
    for term in term_def_dictionary:

        # save the word and definition in user preference list
        word = term.lower()
        v = vocabulary(
            vocabulary = word, 
            definition = term_def_dictionary[term],
            master_list = v_l,
        )
        v.save()
        
        new_term = Term(word, term_def_dictionary[term])

        if not internal_wordbase_vocabulary.objects.filter(vocabulary=new_term.word):
           thread.start_new_thread( parse_and_store_one_term, (new_term,) )

    list_id = v_l.id
    return list_id 
