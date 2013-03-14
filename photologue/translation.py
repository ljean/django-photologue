from modeltranslation.translator import translator, TranslationOptions
from .models import Gallery, Photo

class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Gallery, GalleryTranslationOptions)

class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'caption')

translator.register(Photo, PhotoTranslationOptions)