from django.db import models

######################################
# vocabulary_list
#   purpose:
#     represent a list of vocabularies. when user create a list to study, this is what get created 
# 
# vocabulary
#   purpose: 
#     there exist a bunch of vocabulary user wnats to study, this class represent each words and def
#
######################################
class vocabulary_list(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    creation_date = models.DateField()
    terms = models.IntegerField()
    def __unicode__(self):
        return self.title

class vocabulary(models.Model):

    # word info
    master_list = models.ForeignKey(vocabulary_list)
    vocabulary = models.CharField(max_length=200)
    definition = models.TextField()
    
    # statistic info
    appearance_count = models.IntegerField(default=0)
    right_count = models.IntegerField(default=0)
    wrong_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.vocabulary

class vocabulary_example_sentence(models.Model):

    # word info
    master_vocabulary = models.ForeignKey(vocabulary)
    example_sentences = models.TextField()

    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.example_sentences

class vocabulary_synonyms(models.Model):

    # word info
    master_vocabulary = models.ForeignKey(vocabulary)
    synonyms = models.CharField(max_length=100)
    
    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.synonyms

class vocabulary_extra_definition(models.Model):

    # word info
    master_vocabulary = models.ForeignKey(vocabulary)
    extra_def = models.TextField()

    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.extra_def

######################################
# internal_wordbase_vocabulary
#   purpose:
#     we store internally a word base of vocabularies. so we will have the full information of a word
#     ie. example_sentences, synonyms
# 
# internal_wordbase_vocabulary_example_sentence 
#   purpose: 
#     represent example sentences of a word
#
# internal_wordbase_vocabulary_synonyms
#   purpose:
#     represent synonyms of a word
######################################

class internal_wordbase_vocabulary(models.Model):

    # word info
    vocabulary = models.CharField(max_length=200)
    definition = models.TextField()
    
    # statistic info
    appearance_count = models.IntegerField(default=0)
    right_count = models.IntegerField(default=0)
    wrong_count = models.IntegerField(default=0)
    used_in_list_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.vocabulary

class internal_wordbase_vocabulary_example_sentence(models.Model):
    
    # word info
    master_vocabulary = models.ForeignKey(internal_wordbase_vocabulary)
    example_sentences = models.TextField()
    
    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.example_sentences

class internal_wordbase_vocabulary_synonyms(models.Model):
    
    # word info
    master_vocabulary = models.ForeignKey(internal_wordbase_vocabulary)
    synonyms = models.CharField(max_length=100)
    
    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.synonyms

class internal_wordbase_vocabulary_extra_definition(models.Model):

    # word info
    master_vocabulary = models.ForeignKey(internal_wordbase_vocabulary)
    extra_def = models.TextField()
    
    # statistic info
    selected_count = models.IntegerField(default=0)
    total_appearance_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.extra_def

