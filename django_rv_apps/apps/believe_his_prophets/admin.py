from django.contrib import admin

# Register your models here.
from django_rv_apps.apps.believe_his_prophets.models.testament import Testament
from django_rv_apps.apps.believe_his_prophets.models.language import Language
from django_rv_apps.apps.believe_his_prophets.models.book import Book, BookLanguage
from django_rv_apps.apps.believe_his_prophets.models.version import Version
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.file import File
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapter, SpiritProphecyChapterLanguage
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.application import Application
from django_rv_apps.apps.believe_his_prophets.models.commentary_verse import CommentaryVerse
from django_rv_apps.apps.believe_his_prophets.models.commentary import Commentary
from django_rv_apps.apps.believe_his_prophets.models.emotion import Emotion, LanguageEmotion
from django_rv_apps.apps.believe_his_prophets.models.sentiment import Sentiment, LanguageSentiment
from django_rv_apps.apps.believe_his_prophets.models.analysis_verse import AnalysisVerse, EmotionAnalysisVerse
from django_rv_apps.apps.believe_his_prophets.models.analysis_chapter import AnalysisChapter, EmotionAnalysisChapter
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecyLanguage
from import_export.admin import ImportExportModelAdmin


from import_export import resources


class BibleReadResource(resources.ModelResource):

    class Meta:
        model = BibleRead


class BibleReadAdmin(ImportExportModelAdmin):
    resource_class = BibleReadResource


class BookLanguageInLine(admin.TabularInline):
    model = BookLanguage
    extra = 1


class BookLanguageResource(resources.ModelResource):

    class Meta:
        model = BookLanguage


class BookLanguageAdmin(ImportExportModelAdmin):
    resource_class = BookLanguageResource
    inlines = (BookLanguageInLine,)


class VerseAdmin(admin.ModelAdmin):
    list_display = ['book', 'chapter', 'verse']
    list_filter = ('verse', 'chapter', 'book__book_order', 'language__name',)
    search_fields = ['book__book_order', 'chapter', 'verse', ]


class AnalysisVerseAdmin(admin.ModelAdmin):
    list_display = ['verse']
    list_filter = ('verse', 'verse__language__name',)
    search_fields = ['verse', ]


class CommentaryVerseAdmin(admin.ModelAdmin):
    search_fields = ['verse__book__book_order',
                     'verse__chapter', 'verse__verse', ]
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


class SpiritProphecyChapterLanguageInLine(admin.TabularInline):
    model = SpiritProphecyChapterLanguage
    extra = 1


class SpiritProphecyChapterLanguageAdmin(admin.ModelAdmin):
    inlines = (SpiritProphecyChapterLanguageInLine,)


class SpiritProphecyLanguageInLine(admin.TabularInline):
    model = SpiritProphecyLanguage
    extra = 1


class SpiritProphecyLanguageAdmin(admin.ModelAdmin):
    inlines = (SpiritProphecyLanguageInLine,)


admin.site.register(CommentaryVerse, CommentaryVerseAdmin)
# Register your models here.
admin.site.register(Testament)
admin.site.register(Language)
admin.site.register(Book, BookLanguageAdmin)

admin.site.register(Commentary)
admin.site.register(Version)
admin.site.register(Verse, VerseAdmin)
admin.site.register(BibleRead, BibleReadAdmin)
admin.site.register(SpiritProphecy, SpiritProphecyLanguageAdmin)
admin.site.register(SpiritProphecyChapter, SpiritProphecyChapterLanguageAdmin)
admin.site.register(SpiritProphecyRead)
admin.site.register(Chapter)
admin.site.register(Application)
admin.site.register(Emotion)
admin.site.register(File)
admin.site.register(Sentiment)
admin.site.register(AnalysisVerse, EmotionAnalysisVerseAdmin)
admin.site.register(AnalysisChapter, EmotionAnalysisChapterAdmin)
