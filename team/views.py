# Django Requriments
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.template import RequestContext # for POST
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.conf import settings
from django.utils import simplejson

# Developer Requirements
from team.models import team_member
from team.models import paragraph


#########################################################################
# Page: < Team Page >
# 
# Requests: < display_team(request) > 
#   Description:
#       display team information
#
#   Note:
#       this request still need tunning in the future when we add user
#       log in function
#
#########################################################################

def display_team(request):
    member_list = team_member.objects.all() 
    mem_dictionary_list = []
    for member in member_list:
        member_dictionary = {}
        member_dictionary['name'] = member.name
        member_dictionary['position'] = member.position
        member_dictionary['link'] = member.link
        member_dictionary['image'] = member.image
        paragraph_list = paragraph.objects.filter(master_member=member) 
        para_list = []
        for p in paragraph_list:
            para_dictionary = {}
            para_dictionary['title'] = p.title
            para_dictionary['content'] = p.content
            para_list.append(para_dictionary)

        member_dictionary['paragraph'] = para_list
        mem_dictionary_list.append(member_dictionary)
    return render_to_response(
        'team/display_team.html',
        {
           'members':mem_dictionary_list,
        }
    )
