# -*- coding: utf-8 -*-
from django import template
from django.template.base import Variable, VariableDoesNotExist

register = template.Library()

@register.filter
def first_in_gallery(photo, gallery):
    return (None == photo.get_previous_in_gallery(gallery))