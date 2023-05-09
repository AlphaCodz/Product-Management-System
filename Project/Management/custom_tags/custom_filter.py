from django import template

register = template.Library()

@register.filter
def my_zip(iterable1, iterable2):
    return zip(iterable1, iterable2)