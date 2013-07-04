from BeautifulSoup import BeautifulSoup
from urllib2 import *
import re



from vocabulary_training.models import internal_wordbase_vocabulary
from vocabulary_training.models import internal_wordbase_vocabulary_example_sentence
from vocabulary_training.models import internal_wordbase_vocabulary_synonyms
from vocabulary_training.models import internal_wordbase_vocabulary_extra_definition 
from terms import *

def quick_hack():
    all_words = internal_wordbase_vocabulary.objects.all()
    count = 0
    for word in all_words:
        print count
        count =  count + 1
        try:
            word.vocabulary = str(word.vocabulary)[:-1]
            new_def = internal_wordbase_vocabulary_extra_definition.objects.filter(master_vocabulary=word)[0]
            word.definition = str(new_def)
            word.save()
        except:
            word.vocabulary = str(word.vocabulary)[:-1]
            word.definition = 'none'
            word.save()
            pass

def delete_everything_in_internal_database():
    all_words = internal_wordbase_vocabulary.objects.all()
    count = len(all_words)

    for word in all_words:
        word.delete()
        count = count - 1
        print count


def store_terms_to_database(term_obj_list):

    # Add word to list + Contruct Internal wordbase
    for term in term_obj_list:

        if not internal_wordbase_vocabulary.objects.filter(vocabulary=term.word):
            
            # create new internal_word
            i_v = internal_wordbase_vocabulary(
                vocabulary = term.word,
                definition = term.definition,
            )
            i_v.save()
            
            # add example sentences to the word
            for example in term.examples:
                v_ex = internal_wordbase_vocabulary_example_sentence(
                    master_vocabulary = i_v,
                    example_sentences = term.strip_one_kind_of_html_tag_from_text( 'li',example)
                )
                v_ex.save()
            
            # add synoyms to the word
            for synonym in term.synonyms:
                v_syn = internal_wordbase_vocabulary_synonyms(
                    master_vocabulary = i_v,
                    synonyms = synonym,
                )
                v_syn.save()
            
            # add extra definition
            for defi in term.definitions:
                v_defi = internal_wordbase_vocabulary_extra_definition(
                    master_vocabulary = i_v,
                    extra_def = str(defi),
                )
                v_defi.save()

            # add meanings
            for meaning in term.meanings:
                v_meaning = internal_wordbase_vocabulary_meaning_by_example(
                    master_vocabulary = i_v,
                    meaning_by_example = term.strip_one_kind_of_html_tag_from_text( 'li',meaning),
                )
                v_meaning.save()


def strip_one_kind_of_html_tag_from_text(html_tag, text):
    
    # strip out open tag
    build_pattern = '<' + html_tag + '>'
    pattern = re.compile(build_pattern)
    text = re.sub(pattern, '', str(text))
    
    # strip out close tag	
    build_pattern = '</' + html_tag + '>'
    pattern = re.compile(build_pattern)
    result = re.sub(pattern, '', str(text))
    return result

def construct_term_object_list(file_name):
    term_obj_list = []
    count = 0 
    outfile = open(file_name).read()
    soup = BeautifulSoup(outfile)
    word_list = soup.findAll("div")

    for word in word_list:
        
        w = BeautifulSoup(str(word))
        
        # make sure there is a word, if this failed
        # nothing should be done
        w_list= w.findAll("w")
        if len(w_list):
            _w = strip_one_kind_of_html_tag_from_text('w',w_list[0])
            #print _w
            new_term = Term(_w)
            
            # if we have syn
            s_list = w.findAll("s")
            if len(s_list):
                for s in s_list:
                    _s = strip_one_kind_of_html_tag_from_text('s',s)
                    new_term.add_synonym(_s)

            # if we have an example sentence
            e_list= w.findAll("e")
            if len(e_list):
                for e in e_list:
                    _e = strip_one_kind_of_html_tag_from_text('e',e)
                    new_term.add_example(_e)
            
            # if we have xtra definition
            x_list = w.findAll("x")
            if len(x_list):
                for x in x_list:
                    _x = strip_one_kind_of_html_tag_from_text('x',x)
                    new_term.add_definitions(_x)
            
            # if we have definition
            d_list = w.findAll("d")
            if len(d_list):
                for d in d_list:
                    _d = strip_one_kind_of_html_tag_from_text('d',d)
                    new_term.add_definitions(_d)

            term_obj_list.append(new_term)
			
            if new_term:
	        print new_term
                store_terms_to_database(term_obj_list)
    
    return term_obj_list




def load_each_word_file_into_internal_db():
	
	for i in range(10000):
		some_list = []
		print i
		path_name = '/home/alexwchen/webapps/gre_alex/myproject/create_new_list/out1/word' + str(i+1) + '.txt'

		outfile = open(path_name,'r')        
		tmp = outfile.read()

		w = BeautifulSoup(str(tmp))
		print '-------------------' 
		print i 
		print '-------------------'  
		w_list= w.findAll("w") 
		for _w in w_list:
			_ew = strip_one_kind_of_html_tag_from_text('w',_w)
			new_term = Term(_ew[:-1])

		s_list= w.findAll("s") 
		for s in s_list: 
			_s = strip_one_kind_of_html_tag_from_text('s',s)
			new_term.add_synonym(_s)

		e_list= w.findAll("e")
		for e in e_list:  
			_e = strip_one_kind_of_html_tag_from_text('e',e)
			new_term.add_example(_e)

		x_list = w.findAll("x")
		for x in x_list: 
			_x = strip_one_kind_of_html_tag_from_text('x',x)
			new_term.add_definitions(_x)

		d_list = w.findAll("d") 
		for d in d_list: 
			_d = strip_one_kind_of_html_tag_from_text('d',d)
			new_term.add_definitions(_d)
		
		try:
			new_term.definition = new_term.definitions[0]
			print new_term.definition
		except:
			pass
		print new_term.examples
		print new_term.definitions
		print new_term.synonyms

		some_list.append(new_term)
		store_terms_to_database(some_list)
		outfile.close()
 
