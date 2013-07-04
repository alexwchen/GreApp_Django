from django.contrib import admin

##############################################
# vocabulary_list_Admin
#   purpose:
#     displaying voculary_list in admin
##############################################
from vocabulary_training.models import vocabulary_list
from vocabulary_training.models import vocabulary
from vocabulary_training.models import vocabulary_example_sentence
from vocabulary_training.models import vocabulary_synonyms 
from vocabulary_training.models import vocabulary_extra_definition 

class vocabulary_example_sentence_Inline(admin.StackedInline):
    model = vocabulary_example_sentence
    extra = 0

class vocabulary_synonyms_Inline(admin.StackedInline):
    model = vocabulary_synonyms
    extra = 0

class vocabulary_extra_definition_Inline(admin.StackedInline):
    model = vocabulary_extra_definition 
    extra = 0

class vocabularyInline(admin.TabularInline):
    model = vocabulary
    extra = 0

class vocabulary_list_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['title', 'creation_date', 'authors', 'terms']}),
    ]

    inlines = [vocabularyInline] 

class vocabulary_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['vocabulary', 'definition', 'master_list']}),
        ('Statistics', {'fields':['appearance_count', 'right_count', 'wrong_count']}),
    ]

    inlines = [ vocabulary_extra_definition_Inline,
                vocabulary_synonyms_Inline,
                vocabulary_example_sentence_Inline
                ] 

class vocabulary_extra_definition_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['extra_def', 'master_vocabulary']}),
        ('Statistics', {'fields':['selected_count', 'total_appearance_count']}),
    ]

class vocabulary_example_sentence_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['example_sentences', 'master_vocabulary']}),
        ('Statistics', {'fields':['selected_count', 'total_appearance_count']}),
    ]

class vocabulary_synonyms_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['synonyms', 'master_vocabulary']}),
        ('Statistics', {'fields':['selected_count', 'total_appearance_count']}),
    ]
admin.site.register(vocabulary_list, vocabulary_list_Admin)
admin.site.register(vocabulary, vocabulary_Admin)
admin.site.register(vocabulary_synonyms,vocabulary_synonyms_Admin)
admin.site.register(vocabulary_example_sentence, vocabulary_example_sentence_Admin)
admin.site.register(vocabulary_extra_definition, vocabulary_extra_definition_Admin)

##############################################
# vocabulary_list_Admin
#   purpose:
#     displaying voculary_list in admin
##############################################

from vocabulary_training.models import internal_wordbase_vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary_example_sentence
from vocabulary_training.models import internal_wordbase_vocabulary_synonyms
from vocabulary_training.models import internal_wordbase_vocabulary_extra_definition

class internal_wordbase_vocabulary_extra_definition_Inline(admin.StackedInline):
    model = internal_wordbase_vocabulary_extra_definition
    extra = 0

class internal_wordbase_vocabulary_example_sentence_Inline(admin.StackedInline):
    model = internal_wordbase_vocabulary_example_sentence
    extra = 0

class internal_wordbase_vocabulary_synonyms_Inline(admin.StackedInline):
    model = internal_wordbase_vocabulary_synonyms 
    extra = 0

class internal_wordbase_vocabulary_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Word', {'fields':['vocabulary', 'definition']}),
        ('Statistics', {'fields':['appearance_count', 'right_count', 'wrong_count']}),
    ]

    inlines = [ internal_wordbase_vocabulary_extra_definition_Inline, 
                internal_wordbase_vocabulary_synonyms_Inline,
                internal_wordbase_vocabulary_example_sentence_Inline] 

admin.site.register(internal_wordbase_vocabulary, internal_wordbase_vocabulary_Admin)
