# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.conf import settings
from coop_bar.utils import make_link
from .models import Gallery, GalleryUpload
from django.contrib.contenttypes.models import ContentType

def has_perm(perm_name, model):
    def inner_decorator(func):
        def wrapper(request, context):
            if request and request.user.is_staff and 'gallery' in context:
                ct = ContentType.objects.get_for_model(model)
                perm = '{0}.{2}_{1}'.format(ct.app_label, ct.model, perm_name)
                if request.user.has_perm(perm):
                    return func(request, context)
            return None
        return wrapper
    return inner_decorator

can_add = has_perm("add", GalleryUpload)
can_change = has_perm("change", Gallery)

@can_change
def django_admin_edit_gallery(request, context):
    gallery = context['gallery']
    view_name = 'admin:photologue_gallery_change'
    return make_link(reverse(view_name, args=[gallery.id]), _(u'Photologue: Gallery admin'), 'fugue/image--arrow.png',
        classes=['icon'])

@can_add
def django_admin_add_gallery(request, context):
    gallery = context['gallery']
    view_name = 'admin:photologue_galleryupload_add'
    return make_link(reverse(view_name), _(u'Photologue: Gallery upload'), 'fugue/image--plus.png',
        classes=['icon'])

def load_commands(coop_bar):
    coop_bar.register([
        [django_admin_edit_gallery, django_admin_add_gallery],  
    ])