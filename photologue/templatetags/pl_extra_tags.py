# -*- coding: utf-8 -*-
from django import template
from django.template.base import Variable, VariableDoesNotExist
import os.path
import unicodedata
try:
    from PIL import Image
except ImportError:
    import Image

register = template.Library()

@register.filter
def first_in_gallery(photo, gallery):
    return gallery.photos.first() == photo
    #return (None == photo.get_previous_in_gallery(gallery))

@register.filter
def max_height(gallery, size="display"):
    max_val = 0
    for photo in gallery.photos.all():
        photo_filename = getattr(photo, "get_{0}_filename".format(size))()
        try:
            img = Image.open(photo_filename)
            (w, h) = img.size
            max_val = max(max_val, h)
        except IOError:
            pass
    return max_val
    
@register.filter
def basename(fullname):
    return os.path.basename(fullname)

@register.filter
def normalize_utf8_to_ascii(ustr):
    try:
        return unicodedata.normalize('NFKD', ustr).encode('ascii','ignore')
    except TypeError:
        return ustr
