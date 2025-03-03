from django import template

register = template.Library()

# Custom Filter

def range_filter(value):
    return value[:250]

register.filter('range_filter',range_filter)