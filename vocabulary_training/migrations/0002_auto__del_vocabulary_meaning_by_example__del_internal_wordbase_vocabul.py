# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting model 'vocabulary_meaning_by_example'
        db.delete_table('vocabulary_training_vocabulary_meaning_by_example')

        # Deleting model 'internal_wordbase_vocabulary_meaning_by_example'
        db.delete_table('vocabulary_training_internal_wordbase_vocabulary_meaning_by_example')

        # Adding field 'vocabulary.wrong_count'
        db.add_column('vocabulary_training_vocabulary', 'wrong_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary.right_count'
        db.add_column('vocabulary_training_vocabulary', 'right_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_extra_definition.total_appearance_count'
        db.add_column('vocabulary_training_vocabulary_extra_definition', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_extra_definition.selected_count'
        db.add_column('vocabulary_training_vocabulary_extra_definition', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_example_sentence.total_appearance_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_example_sentence', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_example_sentence.selected_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_example_sentence', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_example_sentence.total_appearance_count'
        db.add_column('vocabulary_training_vocabulary_example_sentence', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_example_sentence.selected_count'
        db.add_column('vocabulary_training_vocabulary_example_sentence', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_extra_definition.total_appearance_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_extra_definition', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_extra_definition.selected_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_extra_definition', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary.wrong_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary', 'wrong_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary.appearance_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary', 'appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary.right_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary', 'right_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary.used_in_list_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary', 'used_in_list_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_synonyms.total_appearance_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_synonyms', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'internal_wordbase_vocabulary_synonyms.selected_count'
        db.add_column('vocabulary_training_internal_wordbase_vocabulary_synonyms', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_synonyms.total_appearance_count'
        db.add_column('vocabulary_training_vocabulary_synonyms', 'total_appearance_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'vocabulary_synonyms.selected_count'
        db.add_column('vocabulary_training_vocabulary_synonyms', 'selected_count', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Adding model 'vocabulary_meaning_by_example'
        db.create_table('vocabulary_training_vocabulary_meaning_by_example', (
            ('master_vocabulary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vocabulary_training.vocabulary'])),
            ('meaning_by_example', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('vocabulary_training', ['vocabulary_meaning_by_example'])

        # Adding model 'internal_wordbase_vocabulary_meaning_by_example'
        db.create_table('vocabulary_training_internal_wordbase_vocabulary_meaning_by_example', (
            ('master_vocabulary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vocabulary_training.internal_wordbase_vocabulary'])),
            ('meaning_by_example', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('vocabulary_training', ['internal_wordbase_vocabulary_meaning_by_example'])

        # Deleting field 'vocabulary.wrong_count'
        db.delete_column('vocabulary_training_vocabulary', 'wrong_count')

        # Deleting field 'vocabulary.right_count'
        db.delete_column('vocabulary_training_vocabulary', 'right_count')

        # Deleting field 'vocabulary_extra_definition.total_appearance_count'
        db.delete_column('vocabulary_training_vocabulary_extra_definition', 'total_appearance_count')

        # Deleting field 'vocabulary_extra_definition.selected_count'
        db.delete_column('vocabulary_training_vocabulary_extra_definition', 'selected_count')

        # Deleting field 'internal_wordbase_vocabulary_example_sentence.total_appearance_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_example_sentence', 'total_appearance_count')

        # Deleting field 'internal_wordbase_vocabulary_example_sentence.selected_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_example_sentence', 'selected_count')

        # Deleting field 'vocabulary_example_sentence.total_appearance_count'
        db.delete_column('vocabulary_training_vocabulary_example_sentence', 'total_appearance_count')

        # Deleting field 'vocabulary_example_sentence.selected_count'
        db.delete_column('vocabulary_training_vocabulary_example_sentence', 'selected_count')

        # Deleting field 'internal_wordbase_vocabulary_extra_definition.total_appearance_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_extra_definition', 'total_appearance_count')

        # Deleting field 'internal_wordbase_vocabulary_extra_definition.selected_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_extra_definition', 'selected_count')

        # Deleting field 'internal_wordbase_vocabulary.wrong_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary', 'wrong_count')

        # Deleting field 'internal_wordbase_vocabulary.appearance_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary', 'appearance_count')

        # Deleting field 'internal_wordbase_vocabulary.right_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary', 'right_count')

        # Deleting field 'internal_wordbase_vocabulary.used_in_list_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary', 'used_in_list_count')

        # Deleting field 'internal_wordbase_vocabulary_synonyms.total_appearance_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_synonyms', 'total_appearance_count')

        # Deleting field 'internal_wordbase_vocabulary_synonyms.selected_count'
        db.delete_column('vocabulary_training_internal_wordbase_vocabulary_synonyms', 'selected_count')

        # Deleting field 'vocabulary_synonyms.total_appearance_count'
        db.delete_column('vocabulary_training_vocabulary_synonyms', 'total_appearance_count')

        # Deleting field 'vocabulary_synonyms.selected_count'
        db.delete_column('vocabulary_training_vocabulary_synonyms', 'selected_count')
    
    
    models = {
        'vocabulary_training.internal_wordbase_vocabulary': {
            'Meta': {'object_name': 'internal_wordbase_vocabulary'},
            'appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'definition': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'used_in_list_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vocabulary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wrong_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.internal_wordbase_vocabulary_example_sentence': {
            'Meta': {'object_name': 'internal_wordbase_vocabulary_example_sentence'},
            'example_sentences': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.internal_wordbase_vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.internal_wordbase_vocabulary_extra_definition': {
            'Meta': {'object_name': 'internal_wordbase_vocabulary_extra_definition'},
            'extra_def': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.internal_wordbase_vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.internal_wordbase_vocabulary_synonyms': {
            'Meta': {'object_name': 'internal_wordbase_vocabulary_synonyms'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.internal_wordbase_vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'synonyms': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.vocabulary': {
            'Meta': {'object_name': 'vocabulary'},
            'appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'definition': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.vocabulary_list']"}),
            'right_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vocabulary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wrong_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.vocabulary_example_sentence': {
            'Meta': {'object_name': 'vocabulary_example_sentence'},
            'example_sentences': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.vocabulary_extra_definition': {
            'Meta': {'object_name': 'vocabulary_extra_definition'},
            'extra_def': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'vocabulary_training.vocabulary_list': {
            'Meta': {'object_name': 'vocabulary_list'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'terms': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vocabulary_training.vocabulary_synonyms': {
            'Meta': {'object_name': 'vocabulary_synonyms'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_vocabulary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vocabulary_training.vocabulary']"}),
            'selected_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'synonyms': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_appearance_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }
    
    complete_apps = ['vocabulary_training']
