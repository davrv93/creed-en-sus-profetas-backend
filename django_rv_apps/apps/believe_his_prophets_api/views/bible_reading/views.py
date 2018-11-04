from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.bible_read import BibleRead
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers\
    import BibleReadSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.filters \
    import BibleReadFilter
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.reading \
    import ReadingMixin
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.mixins.picture \
    import PictureMixin


class ReadingViewSet(viewsets.ModelViewSet, ReadingMixin, PictureMixin):

    queryset = BibleRead.objects.all()
    serializer_class = BibleReadSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BibleReadFilter

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)
