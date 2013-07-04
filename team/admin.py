from django.contrib import admin

##############################################
# vocabulary_list_Admin
#   purpose:
#     displaying voculary_list in admin
##############################################
from team.models import team_member
from team.models import paragraph

class paragraph_Inline(admin.StackedInline):
    model = paragraph 
    extra = 0

class team_member_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['name', 'position', 'link', 'image']}),
    ]

    inlines = [paragraph_Inline] 

class paragrah_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['title', 'content', 'master_member']}),
    ]

admin.site.register(paragraph, paragrah_Admin)
admin.site.register(team_member,team_member_Admin)
