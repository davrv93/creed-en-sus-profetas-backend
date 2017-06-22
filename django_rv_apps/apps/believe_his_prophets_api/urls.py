from django.conf.urls import url, include
from rest_framework import routers
from .views.testament_view import TestamentViewSet
from .views.book_view import BookViewSet
from .views.verse_view import VerseViewSet
from .views.chapter_view import ChapterViewSet
from .views.spirit_prophecy_view import SpiritProphecyViewSet
from .views.spirit_prophecy_chapter_view import SpiritProphecyChapterViewSet
from .views.spirit_prophecy_read_view import SpiritProphecyReadViewSet
from .views.application_view import ApplicationViewSet


router = routers.DefaultRouter()
router.register(r'testament', TestamentViewSet)
router.register(r'book', BookViewSet)
router.register(r'verse', VerseViewSet)
router.register(r'chapter', ChapterViewSet)
router.register(r'spirit_prophecy', SpiritProphecyViewSet)
router.register(r'spirit_prophecy_chapter', SpiritProphecyChapterViewSet)
router.register(r'spirit_prophecy_read', SpiritProphecyReadViewSet)
router.register(r'application', ApplicationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
