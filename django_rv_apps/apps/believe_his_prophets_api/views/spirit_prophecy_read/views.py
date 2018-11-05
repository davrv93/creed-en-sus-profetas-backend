from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers\
    import SpiritProphecyReadSerializer


class SpiritProphecyReadViewSet(viewsets.ModelViewSet, ReadingMixin, PictureMixin):

    queryset = SpiritProphecyRead.objects.all()
    serializer_class = SpiritProphecyReadSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = SpiritProphecyReadFilter

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)
