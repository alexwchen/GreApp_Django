#########################################################################
# File Name: terms.py
# Author: Alexander Chen   
#
# Description:
#   Terms Class allows users to create a term objects, which contain information
#   such as definition, extra_definition, synonyms, example_sentences and so on.
#   It is meant to be an easy interface when crawling data from the web and save it 
#   to our database
#
# Class:
#   Term
#
# Functions:
#
#   [ Add Information to Datastructure ]  
#   add_definitions(self, definition)
#   add_meanings(self, meaning)
#   add_example(self, example)
#   add_synonym(self, synonym)
#
#   [ Set Information to Datastructure ]  
#   set_word(self, word)
#   set_definition(self, definition)
#
#   [ Retrieve information online ]  
#   get_definition_online_given_word(self, word)
#   get_extra_meaning_example_online_given_word(self, word)
#   get_example_sentence_online_given_word(self, word)
#   get_synonyms_online_given_word(self, word)
#
#   [ Retrieve information from Internal Word Database ]
#   [ Used to check if information is already stored ]
#   get_all_example_sentences_given_word(self)
#   get_all_synonyms_given_word(self)
#   get_all_extra_definition_given_word(self)
#   get_all_meanings_given_word(self)
#
#   [ Userful Tools ]  
#   extract_content_between_html_tags(self,html_code)
#   strip_one_kind_of_html_tag_from_text(self, html_tag, text)
#
#
#   Note: Future Development
#   * parse_to_terms_and_def(user_input)
#   This is our only function handle user input data from create,
#   we need to expand this function to its own class in the future
#
#
#
#
#########################################################################

from BeautifulSoup import BeautifulSoup
from urllib2 import *
import re
import os

from vocabulary_training.models import vocabulary_list
from vocabulary_training.models import vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary_example_sentence
from vocabulary_training.models import internal_wordbase_vocabulary_synonyms
from vocabulary_training.models import internal_wordbase_vocabulary_extra_definition 

###########################################################################
# Function Name: 
#   parse_to_terms_and_def(user_input)
#
# Description:
#   This function will take the user input vocabulary list, parse it into 
#   a dictionary 
#
# Note:
#   This function make an unreal assumption about user input. However, for 
#   internal testing, it is enough for now. We need to expand this code into
#   its own class in the future.
#
# Variables:
#   user_input:
#       a bunch of text from textarea in the CREAT page
#
# Returns:
#   dictionary { [word]: definition] }
#
###########################################################################
def parse_to_terms_and_def(user_input):
    result_dict = {}
    user_input = user_input.split('\n')
    for line in user_input:
    	# process regex
        line = line.replace(' ', '@')
        line = line.replace('\t', '@')
        line = line.replace('-', '@')
        result_dict[line.split('@')[0]] = ' '.join(line.split('@')[1:])
    return result_dict

class Term():
    def __init__(self, word="", definition=""):
        self.word = word
        self.definition = definition
        self.examples = []
        self.synonyms = []
        self.definitions = []
        self.meanings = []
    
    def __str__(self):
        return self.word

    def add_definitions(self, definition):
        self.definitions.append(definition)

    def add_meanings(self, meaning):
        self.meanings.append(meaning)

    def add_example(self, example):
        self.examples.append(example)

    def add_synonym(self, synonym):
        self.synonyms.append(synonym)

    def set_word(self, word):
        self.word = word

    def set_definition(self, definition):
        self.definition = definition

###########################################################################
# Function Name: 
#   get_definition_online_given_word(self, word)
#   get_extra_meaning_example_online_given_word(self, word)
#   get_example_sentence_online_given_word(self, word)
#   get_synonyms_online_given_word(self, word)
#
# Description:
#   These function retrieve information from yourdictionary.com base on the
#   word given
#
# Variables:
#   word:
#       word choosed by user
#
# Returns:
#   returns a list of what it found, or empty string "" if any error occoured 
#   in the crawling process
#
###########################################################################
    def get_definition_online_given_word(self, word):
        
        try:
            urlsentence = 'http://www.yourdictionary.com/' + str(word)
            
            html = urlopen(urlsentence).read()
            soup = BeautifulSoup(html)
            example_block = soup.find("div", {'class':'custom_entry'})
            build_pattern = '<div class="custom_entry">.*<span'
            pattern = re.compile(build_pattern)
            text = re.search(build_pattern,str(example_block))
            text = str(text.group()[26:-5])
            return text
        except:
            return ""


    def get_extra_meaning_example_online_given_word(self, word):
        
        try:
            urlsentence = 'http://www.yourdictionary.com/' + str(word)
            
            html = urlopen(urlsentence).read()
            soup = BeautifulSoup(html)
            example_block = soup.find("div", {'class':'custom_entry_example'})
            meanings = example_block.findAll("p")
            if 'li' in str(meanings):
                example_block = soup.find("div", {'class':'custom_entry_example'})
                meanings = example_block.findAll("li")
                return meanings 
            else:
                return meanings
                
        except:
            return ""

    def get_example_sentence_online_given_word(self, word):
        
        try:
            urlsentence = 'http://sentence.yourdictionary.com/' + str(word)
            
            html = urlopen(urlsentence).read()
            soup = BeautifulSoup(html)
            example_block = soup.find("ul", {'class':'example'})
            examples = example_block.findAll("li")

            return examples
        except:
            return ""

    def get_synonyms_online_given_word(self, word):
        try:
            syn_list = []
            urlthesaurus = 'http://thesaurus.yourdictionary.com/' + str(word)
            html = urlopen(urlthesaurus).read()
            soup = BeautifulSoup(html)
            syn_block = soup.find("p", {'class':'syn'})
            synonyms = syn_block.findAll("a")
            for syn in synonyms:
                syn_word = self.extract_content_between_html_tags(syn)
                if syn_word:
                    syn_list.append(syn_word)
            return syn_list
        except:
            return ""
    
###########################################################################
# Function Name: 
#   get_definition_online_given_word(self, word)
#   get_extra_meaning_example_online_given_word(self, word)
#   get_example_sentence_online_given_word(self, word)
#   get_synonyms_online_given_word(self, word)
#
# Description:
#   These function retrieve information from yourdictionary.com base on the
#   word given
#
# Variables:
#   word:
#       word choosed by user
#
# Returns:
#   returns a list of what it found, or empty string "" if any error occoured 
#   in the crawling process
#
###########################################################################
    def get_all_example_sentences_given_word(self):
        master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=self.word)    
        exp = internal_wordbase_vocabulary_example_sentence.objects.filter(master_vocabulary=master_v)    
        print exp
        return exp

    def get_all_synonyms_given_word(self):
        master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=self.word)    
        syn = internal_wordbase_vocabulary_synonyms.objects.filter(master_vocabulary=master_v)    
        return syn

    def get_all_extra_definition_given_word(self):
        master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=self.word)    
        extra = internal_wordbase_vocabulary_extra_definition.objects.filter(master_vocabulary=master_v)    
        return extra

    def get_all_meanings_given_word(self):
        master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=self.word)    
        meaning = internal_wordbase_vocabulary_meaning_by_example.objects.filter(master_vocabulary=master_v)    
        return meaning
    #########################################
    #
    #   General Html Operation Function
    #
    #########################################
    
###########################################################################
# Function Name: 
#   extract_content_between_html_tags(self,html_code)
#
# Description:
#   extract any conetent beween 2 html tags.
#   ie.
#       <a> this is what we want </a>
#
# Variables:
#   code you want to strip:
#
# Returns:
#   if you feed this  <a> this is what we want </a>
#   "this is what we want" will be returned
#
###########################################################################
    def extract_content_between_html_tags(self,html_code):
        pattern = re.compile(r'>.*?<')
        result = re.search(pattern,str(html_code))
        result = str(result.group()[1:-1])
        return result	
    
    
###########################################################################
# Function Name: 
#
# Description:
#   strip one kind of html tag out of a sentence, this is used for sentences 
#   that are nested with different html tags, such as "<p><li>hi</li></p>
#
# Variables:
#	input: 'li', 'randon_txt'
#
# Returns:
#	ie.
#		output: one set of <li> and </li> will be gone
#
###########################################################################
    def strip_one_kind_of_html_tag_from_text(self, html_tag, text):
        
        # strip out open tag
        build_pattern = '<' + html_tag + '>'
        pattern = re.compile(build_pattern)
        text = re.sub(pattern, '', str(text))
        
        # strip out close tag	
        build_pattern = '</' + html_tag + '>'
        pattern = re.compile(build_pattern)
        result = re.sub(pattern, '', str(text))
        return result
    
#urldef = 'http://www.yourdictionary.com/' + 'aberrant'
