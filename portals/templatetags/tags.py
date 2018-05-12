from django import template
from portals.forms import CreateForm
register = template.Library()

@register.inclusion_tag('portals/navbar.html')
def show_bar():
    return {'form':CreateForm}