from modeltranslation.translator import register, TranslationOptions
from news.models import News


@register(News)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
