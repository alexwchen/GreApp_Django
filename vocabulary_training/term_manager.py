#########################################################################
# File Name: term_manager.py
# Author: Alexander Chen   
#
# Description:
#   Term_Manager serves as an interface for accessing database
#   functions are created to access different information from 
#   different database
#
# Class:
#   Term_Manager
#
# Functions:
#
#   [ Not sure where these are used: Functions for retrieving information ]  
#   get_all_vocabulary_lists(self)
#   get_term_obj_list_from_database(self)
#
#   [ Used By Study Page ]  
#   store_extra_definition_in_user_vocabulary_list(self, author, word, content)
#   store_vocabulary_synonyms_in_user_vocabulary_list(self, author, word, content)
#   store_vocabulary_example_sentence_in_user_vocabulary_list(self, author, word, content)
#   store_additional_information_given_vocabulary_and_vocabulary_list(self, author, word, original, modified, category)
#   store_vocabulary_definition_given_vocabulary_and_vocabulary_list(self, author, word, modified)
#   store_vocabulary_name_given_vocabulary_and_vocabulary_list(self, author, word, modified)
#   delete_vocabulary_and_recreate_given_word(self, author, word)
#   delete_vocabulary_recreate_given_word(self, author, list_name, word)
#
#
#   Note: Future Development
#       Plan to create a new class cover all the function that the create page will need
#       Also need to merge the function from term class
#           * parse_to_terms_and_def(user_input)
#
#
#########################################################################
from vocabulary_training.models import vocabulary_list
from vocabulary_training.models import vocabulary
from vocabulary_training.models import vocabulary_example_sentence 
from vocabulary_training.models import vocabulary_synonyms 
from vocabulary_training.models import vocabulary_extra_definition 

from vocabulary_training.models import internal_wordbase_vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary_example_sentence
from vocabulary_training.models import internal_wordbase_vocabulary_synonyms
from vocabulary_training.models import internal_wordbase_vocabulary_extra_definition 

from terms import Term
import datetime

class Term_Manager():
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def get_all_vocabulary_lists(self):
        return vocabulary_list.objects.all() 
    
    def get_term_obj_list_from_database(self, list_id):
        master_list = vocabulary_list.objects.get(title = self.title, id = list_id)
        vocabs = vocabulary.objects.filter(master_list = master_list ).order_by('vocabulary')

        term_obj_list = []
        for vocab in vocabs:
            term = Term(vocab.vocabulary, vocab.definition)
            
            # add extra definition
            defis = vocabulary_extra_definition.objects.filter(master_vocabulary=vocab).order_by('extra_def')
            for defi in defis:
                term.add_definitions(defi)
            # add synonyms
            syns = vocabulary_synonyms.objects.filter(master_vocabulary=vocab).order_by('synonyms')
            for syn in syns:
                term.add_synonym(syn)
            # add example sentences
            exps = vocabulary_example_sentence.objects.filter(master_vocabulary=vocab).order_by('example_sentences')
            for exp in exps:
                term.add_example(exp)

            term_obj_list.append(term)
        return term_obj_list
    

###########################################################################
# Function Name: 
#   store_extra_definition_in_user_vocabulary_list(self, author, word, content):
#   store_vocabulary_synonyms_in_user_vocabulary_list(self, author, word, content):
#   store_vocabulary_example_sentence_in_user_vocabulary_list(self, author, word, content):
#   store_additional_information_given_vocabulary_and_vocabulary_list(self, author, word, original, modified, category):
#   store_vocabulary_name_given_vocabulary_and_vocabulary_list(self, author, word, modified):
#   delete_vocabulary_and_recreate_given_word(self, author, word):
#
# Description:
#   Used in Study Page. These functions are all created for user to change their preference information
#   in the study page. These information will be used in Training and Testing mode.
#
###########################################################################
    def store_extra_definition_in_user_vocabulary_list(self, author, word, content):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            if len(vocabulary_extra_definition.objects.filter(master_vocabulary=master_vWord, extra_def=content))==0:
                extra_def = vocabulary_extra_definition(master_vocabulary=master_vWord, extra_def=content)
                extra_def.save()
            else:
                pass
        except:
            message = False
            
        return message

    
    def store_vocabulary_synonyms_in_user_vocabulary_list(self, author, word, content):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            if len(vocabulary_synonyms.objects.filter(master_vocabulary=master_vWord, synonyms=content))==0:
                synonym = vocabulary_synonyms(master_vocabulary=master_vWord, synonyms=content)
                synonym.save()
            else:
                pass
        except:
            message = False
            
        return message
    
    def store_vocabulary_example_sentence_in_user_vocabulary_list(self, author, word, content):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            if len(vocabulary_example_sentence.objects.filter(master_vocabulary=master_vWord,
            example_sentences=content))==0:
                example = vocabulary_example_sentence(master_vocabulary=master_vWord, example_sentences=content)
                example.save()
            else:
                pass
        except:
            message = False
            
        return message
    
    def delete_vocabulary_and_recreate_given_word(self, author, word):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            defi = master_vWord.definition
            appear_count = master_vWord.appearance_count
            master_vWord.delete()
            master_vWord = vocabulary(master_list=master_vlist, vocabulary=word, definition=defi)
            master_vWord.appearance_count = appear_count
            master_vWord.save()
        except:
            message = False
        return message

    def store_additional_information_given_vocabulary_and_vocabulary_list(self, author, word, original, modified, category):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            if category == "definition":
                defi = vocabulary_extra_definition.objects.get(master_vocabulary=master_vWord, extra_def=original)
                defi.extra_def = modified
                defi.save()
            elif category == "example":
                exp = vocabulary_example_sentence.objects.get(master_vocabulary=master_vWord, example_sentences=original)
                exp.example_sentences = modified
                exp.save()
            elif category == "synonym":
                syn = vocabulary_synonyms.objects.get(master_vocabulary=master_vWord, synonyms=original)
                syn.synonyms = modified
                syn.save()
        except:
            message = False

        return message
    
    def store_vocabulary_definition_given_vocabulary_and_vocabulary_list(self, author, word, modified):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            master_vWord.definition = modified
            master_vWord.save()
        except:
            message = False

        return message

    
    def store_vocabulary_name_given_vocabulary_and_vocabulary_list(self, author, word, modified):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            master_vWord.vocabulary = modified
            master_vWord.save()

        except:
            message = False

        return message

    def delete_vocabulary_recreate_given_word(self, author, word):
        message = True
        try:
            master_vlist = vocabulary_list.objects.get(authors=author, title=self.title)
            master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
            master_vWord.delete()
        except:
            message = False

        return message
