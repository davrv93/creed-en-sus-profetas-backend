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


# Register your models here.
admin.site.register(Testament)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Version)
admin.site.register(Verse)
admin.site.register(BibleRead)
admin.site.register(SpiritProphecy)
admin.site.register(SpiritProphecyChapter)
admin.site.register(SpiritProphecyRead)
admin.site.register(Chapter)
admin.site.register(Application)