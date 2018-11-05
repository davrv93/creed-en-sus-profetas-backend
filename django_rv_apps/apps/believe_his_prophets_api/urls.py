from django.conf.urls import url, include
from rest_framework import routers

from .views.book.views import BookViewSet

from .views.chapter.views import ChapterViewSet

from .views.language.views import LanguageViewSet

from .views.testament.views import TestamentViewSet

from .views.verse.views import VerseViewSet

from .views.spirit_prophecy_view import SpiritProphecyViewSet
from .views.spirit_prophecy_chapter_view import SpiritProphecyChapterViewSet
from .views.spirit_prophecy_read_view import SpiritProphecyReadViewSet
from .views.application_view import ApplicationViewSet
from .views.bible_reading.views import ReadingViewSet

router = routers.DefaultRouter()

router.register(r'bible_reading', ReadingViewSet)
router.register(r'books', BookViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'testaments', TestamentViewSet)
router.register(r'verses', VerseViewSet)
router.register(r'spirit_prophecy', SpiritProphecyViewSet)
router.register(r'spirit_prophecy_chapter', SpiritProphecyChapterViewSet)
router.register(r'spirit_prophecy_read', SpiritProphecyReadViewSet)
router.register(r'application', ApplicationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
   

]
