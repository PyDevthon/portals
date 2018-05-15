from django import template
from portals.forms import CreateForm, UserForm

register = template.Library()


@register.inclusion_tag('portals/navbar.html', takes_context=True)
def show_bar(context):
    request = context['request']
    return {'form_ask':CreateForm(),'request':request}

