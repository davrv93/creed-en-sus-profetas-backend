from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter

from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers\
    import BibleReadSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.filters \
    import BibleReadFilter
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.reading \
    import ReadingMixin
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.picture \
    import PictureMixin

from django_rv_apps.apps.believe_his_prophets_api.views.verse.serializers import VerseSerializer

from django_rv_apps.apps.believe_his_prophets_api.views.book.serializers import BookSerializer

class ReadingViewSet(viewsets.ModelViewSet, ReadingMixin, PictureMixin):

    queryset = BibleRead.objects.all()
    serializer_class = BibleReadSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BibleReadFilter

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)


class BibleReadingView(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = ()

    def get(self, request, format=None):

        retorno = dict()

        date = request.query_params.get('date')

        code_iso = request.query_params.get('code_iso','').upper()

        bible_read = BibleRead.objects.get(start_date=date)

        book = bible_read.book

        serializer = BookSerializer(book, context={
            'code_iso':code_iso
        })

        retorno.update(
            book=serializer.data
        )

        chapter = bible_read.start_chapter

        retorno.update(
            chapter=chapter
        )

        verses = Verse.objects.filter(
            book=book,
            language__code_iso = code_iso,
            chapter = chapter
        )

        serializer = VerseSerializer(
            verses, many=True
        )

        retorno.update(
            verses=serializer.data
        )


        return Response(retorno)