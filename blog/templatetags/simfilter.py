# -*- coding: utf-8 -*-
from django import template
register = template.Library()

def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return '%s@@'%value.upper()

register.filter('lower', lower)