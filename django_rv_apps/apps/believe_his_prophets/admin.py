from django.contrib import admin

# Register your models here.
from django_rv_apps.apps.believe_his_prophets.models.testament import Testament
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.version import Version
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.application import Application
from django_rv_apps.apps.believe_his_prophets.models.commentary_verse import CommentaryVerse
from django_rv_apps.apps.believe_his_prophets.models.commentary import Commentary
from django_rv_apps.apps.believe_his_prophets.models.emotion import Emotion, LanguageEmotion
from django_rv_apps.apps.believe_his_prophets.models.sentiment import Sentiment, LanguageSentiment
from django_rv_apps.apps.believe_his_prophets.models.analysis_verse import AnalysisVerse, EmotionAnalysisVerse
from django_rv_apps.apps.believe_his_prophets.models.analysis_chapter import AnalysisChapter, EmotionAnalysisChapter

class VerseAdmin(admin.ModelAdmin):
    list_display = ['book', 'chapter', 'verse']
    list_filter = ('verse','chapter','book__name','language__name',)
    search_fields = ['book__name', 'book__book_order','chapter','verse',]


class AnalysisVerseAdmin(admin.ModelAdmin):
    list_display = ['verse']
    list_filter = ('verse','verse__language__name',)
    search_fields = ['verse',]


class CommentaryVerseAdmin(admin.ModelAdmin):
    search_fields = ['verse__book__book_order','verse__chapter','verse__verse',]
    raw_id_fields = ('verse',)

class EmotionAnalysisVerseInLine(admin.TabularInline):
    model = EmotionAnalysisVerse
    extra = 1


class EmotionAnalysisVerseAdmin(admin.ModelAdmin):
    inlines = (EmotionAnalysisVerseInLine,)

class EmotionAnalysisChapterInLine(admin.TabularInline):
    model = EmotionAnalysisChapter
    extra = 1


class EmotionAnalysisChapterAdmin(admin.ModelAdmin):
    inlines = (EmotionAnalysisChapterInLine,)


admin.site.register(CommentaryVerse, CommentaryVerseAdmin)
# Register your models here.
admin.site.register(Testament)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Commentary)
admin.site.register(Version)
admin.site.register(Verse, VerseAdmin)
admin.site.register(BibleRead)
admin.site.register(SpiritProphecy)
admin.site.register(SpiritProphecyChapter)
admin.site.register(SpiritProphecyRead)
admin.site.register(Chapter)
admin.site.register(Application)
admin.site.register(Emotion)
admin.site.register(Sentiment)
admin.site.register(AnalysisVerse, EmotionAnalysisVerseAdmin)
admin.site.register(AnalysisChapter, EmotionAnalysisChapterAdmin)



