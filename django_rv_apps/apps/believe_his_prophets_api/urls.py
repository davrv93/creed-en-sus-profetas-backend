from django.conf.urls import url, include
from rest_framework import routers
from django_rv_apps.apps.believe_his_prophets_api.views.book_language.views import BookLanguageViewSet
from .views.book.views import BookViewSet

from .views.chapter.views import ChapterViewSet

from .views.language.views import LanguageViewSet

from .views.testament.views import TestamentViewSet
from django.views.decorators.csrf import csrf_exempt

from .views.verse.views import VerseViewSet

from .views.spirit_prophecy_view import SpiritProphecyViewSet
from .views.spirit_prophecy_chapter_view import SpiritProphecyChapterViewSet
from .views.spirit_prophecy_read_view import SpiritProphecyReadViewSet
from .views.application_view import ApplicationViewSet
from .views.bible_reading.views import ReadingViewSet
from .views.bible_reading.views import BibleReadingView
from .views.bible_reading.views import AudioView

from .views.spirit_prophecy_chapter_language.views import SpiritProphecyChapterLanguageViewSet

router = routers.DefaultRouter()

router.register(r'bible_reading', ReadingViewSet)
router.register(r'books', BookViewSet)
router.register(r'book_languages', BookLanguageViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'testaments', TestamentViewSet)
router.register(r'verses', VerseViewSet)
router.register(r'spirit_prophecy', SpiritProphecyViewSet)
router.register(r'spirit_prophecy_chapter', SpiritProphecyChapterViewSet)
router.register(r'spirit_prophecy_read', SpiritProphecyReadViewSet)
router.register(r'spirit_prophecy_chapter_language',
                SpiritProphecyChapterLanguageViewSet)


router.register(r'application', ApplicationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^bible_readings/$',BibleReadingView.as_view(), name='bible_readings'),
    url(r'^audio/$',csrf_exempt(AudioView.as_view()), name='audio'),

]
