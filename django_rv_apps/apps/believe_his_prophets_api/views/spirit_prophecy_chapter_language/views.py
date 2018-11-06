from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapterLanguage
from django_rv_apps.apps.believe_his_prophets_api.views.spirit_prophecy_chapter_language.serializer\
    import SpiritProphecyChapterLanguageSerializer
from django_rv_apps.apps.believe_his_prophets_api.views.spirit_prophecy_chapter_language.filters\
    import SpiritProphecyChapterLanguageFilter


class SpiritProphecyChapterLanguageViewSet(viewsets.ModelViewSet):

    queryset = SpiritProphecyChapterLanguage.objects.all()
    serializer_class = SpiritProphecyChapterLanguageSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = SpiritProphecyChapterLanguageFilter

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)
