from django import template 

# this is where all tags and filter are registered
register = template.Library()

@register.filter
def term_title_to_url(term_title):
    return str(term_title).replace(' ', '_')


