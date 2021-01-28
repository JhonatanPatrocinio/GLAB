import re
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    try:
        pattern = '^' + reverse(url_name)
    except NoReverseMatch:
        pattern = url_name
    path = context['request'].path
    return 'active' if re.search(pattern, path) else ''
