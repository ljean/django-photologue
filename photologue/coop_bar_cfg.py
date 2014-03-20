# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.conf import settings
from coop_bar.utils import make_link

def django_admin_edit_gallery(request, context):
    if request and request.user.is_staff and 'gallery' in context:
        gallery = context['gallery']
        view_name = 'admin:photologue_gallery_change'
        return make_link(reverse(view_name, args=[gallery.id]), _(u'Photologue: Gallery admin'), 'fugue/image.png',
            classes=['icon', 'alert_on_click'])

def django_admin_add_gallery(request, context):
    if request and request.user.is_staff and 'gallery' in context:
        gallery = context['gallery']
        view_name = 'admin:photologue_gallery_add'
        return make_link(reverse(view_name), _(u'Photologue: Gallery add'), 'fugue/image.png',
            classes=['icon', 'alert_on_click'])

def load_commands(coop_bar):
    coop_bar.register([
        [django_admin_edit_gallery, django_admin_add_gallery],  
    ])