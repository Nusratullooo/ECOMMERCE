from modeltranslation.translator import register, TranslationOptions
from home.models import Information, Aboutus, FAQ, Slider


@register(Information)
class InformationTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'description',)


@register(Aboutus)
class AboutusTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
