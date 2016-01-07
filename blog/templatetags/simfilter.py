# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter(name='Category_LR')
def Category_LR(value,arg): # Only one argument.
    """category as left or right"""
    value_len = len(value)/2
    left_value = value[0:value_len]
    if (value_len % 2) == 0:
       left_value = value[0:value_len]
       right_value = value[value_len:len(value)]
    else:
       left_value = value[0:value_len+1]
       right_value = value[value_len+1:len(value)]
    category_dic = {'left_value':left_value, 'right_value':right_value}
    return category_dic[arg]
