from django import template
from portals.forms import CreateForm


register = template.Library()


@register.inclusion_tag('portals/navbar.html', takes_context=True)
def show_bar(context):
    request = context['request']
    return {'form_ask':CreateForm(),'request':request}


@register.simple_tag(name='check')
def check(user_id, item):
    if user_id in item.get_voted_by():
        return False
    return True
