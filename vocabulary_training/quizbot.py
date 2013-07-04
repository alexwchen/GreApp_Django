#########################################################################
# File Name: quizbot.py
# Author: Alexander Chen   
#
# Description:
#   Funcions written in this file are mostly related to producing questoins
#   for training and testing the user. 
#
# Class:
#   Quizbot
#
# Functions:
#
# [ Accessing Inernal Word Database ]  
# get_word_list(self)
# get_random_word_in_list(self)
# get_definition_given_word(self, word)
# get_random_example_sentence_given_word(self,word)
# get_random_synonym_given_word(self,word)
#
# questoins_ask_definition_choose_word(self, word)
# questoins_ask_example_sentence_choose_word(self, word)
# questoins_ask_synonym_choose_word(self, word)
#
# [ Accessing User Preference Database ]  
# get_random_user_preference_definition_given_word(self, word)
# get_random_user_preference_example_sentence_given_word(self,word)
# get_random_user_preference_synonym_given_word(self,word)
# get_random_user_preference_question_given_word(self, word):
#
# [ Generating Questions ]  
# generate_multiple_choices_word(self, how_many, word)
# sub_out_answer_key_to_blank_in_a_sentence(self,sentence)
# strip_out_answer_key_word_from_a_sentence_case_insensative(self, sentence, word):
# make_a_question_given_answer_question_dictionary(self, QA_dictionary, type_of_questions):
#
# [ Called By View ]
#
# get_a_list_of_questions_given_amount_and_type(self, num_questions, type_of_questions):
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

import math
import re
import random

class Quizbot():
    def __init__(self, list_title, author):
        self.list_title = list_title
        self.author = author

        # construct word_list
        self.master_list = vocabulary_list.objects.filter(title=list_title, authors=author)[0]
        self.word_list = vocabulary.objects.filter(master_list=self.master_list).order_by("vocabulary")
        self.list_length = len(self.word_list)

    def __str__(self):
        return self.list_title

    def get_word_list(self):
        new_word_list = []
        for word in self.word_list:
            new_word_list.append(word.vocabulary)
        return new_word_list

    def get_random_word_in_list(self):
        rand_idx = math.floor(random.random() * self.list_length) 
        return str(self.word_list[int(rand_idx)])
    
    def generate_multiple_choices_word(self, how_many, word):
        count = 0
        choices = []
        while (count < how_many):
            new_word = self.get_random_word_in_list()
            if new_word!=word:
                choices.append(new_word)
                count = count + 1
        return choices
    
    def get_a_list_based_on_word_appearance_count(self, amount):
        word_list = []
        all_words = vocabulary.objects.filter(master_list=self.master_list).order_by('appearance_count')[1:amount]
        for word in all_words:
            word_list.append((word.vocabulary, word.appearance_count))
        return word_list


    ###########################################################################
    # Function Name: 
    #   sub_out_answer_key_to_blank_in_a_sentence
    #
    # Description:
    #   Replace conetent beween <strong> </strong>, which happens to be 
    #	the word we expect user to answer
    #
    # Variables:
    #   sentence:
    #       a word choose by the user
    #
    # Returns:
    #   definition, synonym or example_sentence depends on the function name:
    #
    ###########################################################################
    def sub_out_answer_key_to_blank_in_a_sentence(self,sentence):
        answer_key = re.compile(r'<strong>.*?</strong>')
        result = re.sub(answer_key, '_________ ', str(sentence))
        result = result.replace('\n', '')
        return result	

    ###########################################################################
    # Function Name: 
    #  strip_out_answer_key_word_from_a_sentence_case_insensative(self, sentence) 
    #
    # Description:
    #  strip out all the answer key case not sensative. 
    #
    # Variables:
    #   sentence:
    #       a word choose by the user
    #       "alex", "Alex", "ALEX", will all get strip out if we are searching for Alex
    # Returns:
    #   answer that will be answered by the user
    #
    ###########################################################################
    def strip_out_answer_key_word_from_a_sentence_case_insensative(self, sentence, word):
        
        # strip out <strong> tag, replace with '_______'
        tag_striped = self.sub_out_answer_key_to_blank_in_a_sentence(sentence) 

        # split the original sentence
        new_sentence = tag_striped.split(' ')
        result_list= []
        for each_word in new_sentence:
            strip_word = re.sub(r'[^\w]', ' ', each_word)
            # compare each word in the split sentence to the original word, replace to _____ if they are the same
            if strip_word.lower() == word.lower():
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            elif strip_word.lower() == word.lower()+'s':
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            elif strip_word.lower() == word.lower()+'d':
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            elif strip_word.lower() == word.lower()+'ed':
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            elif strip_word.lower() == word.lower()+'.':
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            elif strip_word.lower() == word.lower()+';':
                each_word = re.sub(r'[A-Za-z]', '_', each_word)

            result_list.append(each_word)
        result = ' '.join(result_list)
        return result

    ###########################################################################
    # Function Name: 
    #   get_definition_given_word(self, word):
    #   get_random_extra_definition_given_word(self, word):
    #   get_random_example_sentence_given_word(self,word):
    #   get_random_synonym_given_word(self,word):
    #
    # Description:
    #   These three function basically do the same thing. Retrieve a random 
    #   [definition | example sentence | synonym ] out of user internal word database
    #
    # Variables:
    #   word:
    #       a word choose by the user
    #
    # Returns:
    #   definition, synonym or example_sentence depends on the function name:
    #
    ###########################################################################

    # [ Accessing Inernal Word Database ]  
    def get_definition_given_word(self, word):
        try:
            defi = vocabulary.objects.filter(vocabulary=word)[0]
            return str(defi.definition)
        except:
            return []

    # [ Accessing Inernal Word Database ]  
    def get_random_extra_definition_given_word(self, word):
        try:
            master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=word)    
            extra_defi = internal_wordbase_vocabulary_extra_definition.objects.filter(master_vocabulary=master_v)
            if len(extra_defi)==0:
                return extra_defi
            else:
                rand_idx = math.floor(random.random() * len(extra_defi))
                return str(extra_defi[int(rand_idx)])
        except:
            return []

    # [ Accessing Inernal Word Database ]  
    def get_random_example_sentence_given_word(self,word):
        try:
            master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=word)    
            exp = internal_wordbase_vocabulary_example_sentence.objects.filter(master_vocabulary=master_v)    
            if len(exp)==0:
                return exp
            else:
                rand_idx = math.floor(random.random() * len(exp))
                return str(exp[int(rand_idx)])
        except:
            return []

    # [ Accessing Inernal Word Database ]  
    def get_random_synonym_given_word(self,word):
        try:
            master_v = internal_wordbase_vocabulary.objects.filter(vocabulary=word)
            sym = internal_wordbase_vocabulary_synonyms.objects.filter(master_vocabulary=master_v)    
            if len(sym)==0:
                return sym
            else:
                rand_idx = math.floor(random.random() * len(sym))
                return str(sym[int(rand_idx)])
        except:
            return []
    
    # [ Accessing Inernal Word Database ]  
    def questoins_ask_definition_choose_word(self, word):
        defi = self.get_definition_given_word(word)
        options = self.generate_multiple_choices_word(3, word)
        count = 1
        tuplist = [(str(count),str(word))]
        count = count + 1
        for op in options:
            tuplist.append((str(count),str(op)))    
            count = count + 1
        random.shuffle(tuplist)
        tuptup = (tuplist[0], tuplist[1], tuplist[2], tuplist[3])
        return defi, tuptup
    
    # [ Accessing Inernal Word Database ]  
    def questoins_ask_example_sentence_choose_word(self, word):
        exp = self.get_random_example_sentence_given_word(word)
        exp = exp.replace('\n', ' ')
        exp = self.sub_out_answer_key_to_blank_in_a_sentence(exp)
        options = self.generate_multiple_choices_word(3, word)
        count = 1
        tuplist = [(str(count),str(word))]
        count = count + 1
        for op in options:
            tuplist.append((str(count),str(op)))    
            count = count + 1
        random.shuffle(tuplist)
        tuptup = (tuplist[0], tuplist[1], tuplist[2], tuplist[3])
        return exp, tuptup

    # [ Accessing Inernal Word Database ]  
    def questoins_ask_synonym_choose_word(self, word):
        sym = self.get_random_synonym_given_word(word)
        options = self.generate_multiple_choices_word(3, word)
        count = 1
        tuplist = [(str(count),str(word))]
        count = count + 1
        for op in options:
            tuplist.append((str(count),str(op)))    
            count = count + 1
        random.shuffle(tuplist)
        tuptup = (tuplist[0], tuplist[1], tuplist[2], tuplist[3])
        return sym, tuptup
    
    
    
    ###########################################################################
    # Function Name: 
    #   get_random_user_preference_definition_given_word(self, word)
    #   get_random_user_preference_extra_definition_given_word(self, word)
    #   get_random_user_preference_example_sentence_given_word(self,word)
    #   get_random_user_preference_synonym_given_word(self,word)
    #
    # Description:
    #   These three function basically do the same thing. Retrieve a random 
    #   [definition | example sentence | synonym ] out of user preference list(Vocabulary)
    #   under each vocabulary list
    #
    # Variables:
    #   word:
    #       a word choose by the user
    #
    # Returns:
    #   definition, synonym or example_sentence depends on the function name:
    #
    ###########################################################################

    # [ Accessing User Preference Database ]  
    def get_random_user_preference_definition_given_word(self, word):
        master_vlist = vocabulary_list.objects.get(title=self.list_title, authors=self.author)
        master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
        defs = str(master_vWord.definition)
        # user did not select any definition preference, thus we get a random one
        if len(defs) == 0:
            before_strip = str(get_definition_given_word(word))
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip

        # user did select something, choose a random one for them
        else:
            before_strip = defs
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip


    # [ Accessing User Preference Database ]  
    def get_random_user_preference_extra_definition_given_word(self, word):
        master_vlist = vocabulary_list.objects.get(title=self.list_title, authors=self.author)
        master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
        extra_defs = vocabulary_extra_definition.objects.filter(master_vocabulary=master_vWord)
        # user did not select any definition preference, thus we get a random one
        if len(extra_defs) == 0:
            before_strip = str(self.get_random_extra_definition_given_word(word))
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip

        # user did select something, choose a random one for them
        else:
            rand_idx = math.floor(random.random() * len(extra_defs))
            before_strip = str(extra_defs[int(rand_idx)])
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip

    # [ Accessing User Preference Database ]  
    def get_random_user_preference_example_sentence_given_word(self,word):
        master_vlist = vocabulary_list.objects.get(title=self.list_title, authors=self.author)
        master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
        exp = vocabulary_example_sentence.objects.filter(master_vocabulary=master_vWord)
        # user did not select any definition preference, thus we get a random one
        if len(exp) == 0:
            before_strip = str(self.get_random_example_sentence_given_word(word))
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip
        # user did select something, choose a random one for them
        else:
            rand_idx = math.floor(random.random() * len(exp))
            before_strip = str(exp[int(rand_idx)])
            after_strip = self.strip_out_answer_key_word_from_a_sentence_case_insensative(before_strip,word) 
            return after_strip

    # [ Accessing User Preference Database ]  
    def get_random_user_preference_synonym_given_word(self,word):
        master_vlist = vocabulary_list.objects.get(title=self.list_title, authors=self.author)
        master_vWord = vocabulary.objects.get(master_list=master_vlist, vocabulary=word)
        syn = vocabulary_synonyms.objects.filter(master_vocabulary=master_vWord)
        # user did not select any definition preference, thus we get a random one
        if len(syn) == 0:
            selected = str(self.get_random_synonym_given_word(word))
            if len(selected)==2:
                return []
            else:
                return "which word has the same meaning as this word? [ _____ " + selected + "______ ]"
        # user did select something, choose a random one for them
        else:
            rand_idx = math.floor(random.random() * len(syn))
            selected = str(syn[int(rand_idx)])
            if len(selected)==2:
                return []
            else:
                return "which word has the same meaning as this word? [ _____ " + selected + "______ ]"

    # [ Accessing User Preference Database ]  - Get Any of the above
    def get_random_user_preference_question_given_word(self, word):
        rand_int = int(random.random()*4)+1
        #get definition
        if rand_int == 1:
            question = self.get_definition_given_word(word)
        # get extra def
        elif rand_int == 2:
            question = self.get_random_user_preference_extra_definition_given_word(word)
        #get example sentence
        elif rand_int == 3:
            question = self.get_random_user_preference_example_sentence_given_word(word)
        # get synonyms    
        elif rand_int == 4:
            question = self.get_random_user_preference_synonym_given_word(word)
        elif rand_int == 5:
            question = self.get_random_user_preference_extra_definition_given_word(word)
        else:
            question = 'Sorry, there appear to be some error, please complain and let us know.'
        return question

    ###########################################################################
    # Function Name: make_a_question_given_answer_question_dictionary
    #
    # Description:
    #   Make a question data structure
    #
    # Variables:
    #   QA_dictoinary:
    #       a dictionary looks like this {[word], [question]}
    #
    #   type_of_questions: (String)
    #       definition
    #       extra_definition
    #       example_sentence
    #       synonym
    # Returns:
    #   Op_dictionary:
    #       a dictoinary looks like this, {[question]:[option tuples]}
    #
    ###########################################################################

    def make_a_question_given_answer_question_dictionary(self, QA_dictionary, type_of_questions):
        Op_dictionary = {}
        for word in QA_dictionary:
            # generate 3 other options and label them, label=1 will be the answer.
            # this allows user varify their choice in javascript
            options = self.generate_multiple_choices_word(3, word)
            count = 1
            tuplist = [(str(count),str(word))]
            count = count + 1
            for op in options:
                tuplist.append((str(count),str(op)))    
                count = count + 1
            random.shuffle(tuplist)
            tuptup = (tuplist[0], tuplist[1], tuplist[2], tuplist[3])
            Op_dictionary[QA_dictionary[word]] = tuptup
        return Op_dictionary

    ###########################################################################
    # Function Name: get_a_list_of_questions_given_amount_and_type
    #
    # Description:
    #   Return a list of questoins in dictoinary form, caller can decide how long the list shoud be
    #
    # Variables:
    #   num_question:
    #       any number is good
    #
    #   type_of_questions: (String)
    #       definition
    #       extra_definition
    #       example_sentence
    #       synonym
    # Returns:
    #   Op_dictionary:
    #       a dictoinary looks like this, {[question]:[option tuples]}
    #
    ###########################################################################
    def get_a_list_of_questions_given_amount_and_type(self, num_questions, type_of_questions):
        QA_dictionary = {}

        count = 0
        
        """ 
        All these words are fix, is the less appeared words
        """ 
        fix_word_count = int(num_questions*0.7)
        wordlist = self.get_a_list_based_on_word_appearance_count(fix_word_count)
        print wordlist
        for word in wordlist:
            # get a question according to question type
            if type_of_questions=="definition":
                question = self.get_random_user_preference_definition_given_word(word[0])
            elif type_of_questions=="extra_definition":
                question = self.get_random_user_preference_extra_definition_given_word(word[0])
            elif type_of_questions=="example_sentence":
                question = self.get_random_user_preference_example_sentence_given_word(word[0])
            elif type_of_questions=="synonym":
                question = self.get_random_user_preference_synonym_given_word(word[0])
            elif type_of_questions=="mix":
                question = self.get_random_user_preference_question_given_word(word[0])
                 
            # store in the dictionary only if we get something
            if len(question)>2 and (question not in QA_dictionary.values()):
                QA_dictionary[word[0]] = question 
                count = count + 1
            else:
               pass


        """ 
        The rest of the words will be random
        """ 
        while count < num_questions:
            question = ""
            # get a random word
            rand_word = self.get_random_word_in_list()
            
            # make sure random word is not in the QA_dictoinary list
            if rand_word not in QA_dictionary.keys():

                # get a question according to question type
                if type_of_questions=="definition":
                    question = self.get_random_user_preference_definition_given_word(rand_word)
                elif type_of_questions=="extra_definition":
                    question = self.get_random_user_preference_extra_definition_given_word(rand_word)
                elif type_of_questions=="example_sentence":
                    question = self.get_random_user_preference_example_sentence_given_word(rand_word)
                elif type_of_questions=="synonym":
                    question = self.get_random_user_preference_synonym_given_word(rand_word)
                elif type_of_questions=="mix":
                    question = self.get_random_user_preference_question_given_word(rand_word)
                
                     
                # store in the dictionary only if we get something
                if len(question)>2 and (question not in QA_dictionary.values()):
                    QA_dictionary[rand_word] = question 
                    count = count + 1
                else:
                    pass

        Op_dictionary = self.make_a_question_given_answer_question_dictionary(QA_dictionary, type_of_questions)
        print Op_dictionary
        print len(Op_dictionary)

        """
        Statistic Manipulation Starts Here
        """
        # update appearance count
        # this will help us retrieve the word based on probability
        for question in Op_dictionary:
            options = Op_dictionary[question]
            for option in options:
                if option[0]=='1':
                    answer_word = vocabulary.objects.get(master_list=self.master_list, vocabulary=option[1])
                    answer_word.appearance_count = answer_word.appearance_count + 1
                    answer_word.save()
        return Op_dictionary


