from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from django.db.models import F,  Value as V, When, CharField, Case

from django.db.models.functions import Concat

from django_rv_apps.apps.believe_his_prophets.models.hierarchy import Hierarchy
from .serializers import HierarchySerializer
from .filters import HierarchyFilter


class HierarchyViewSet(viewsets.ModelViewSet):

    queryset = Hierarchy.objects.select_related(
        'entity__hierarchy_type',
        'sucursal',
        'entity'
    ).annotate(
        nombre=Concat(
            'entity__hierarchy_type__name',
            V(' '),
            Case(
                When(entity__hierarchy_type__connector__isnull=False,
                     then=F('entity__hierarchy_type__connector')),
                default=V(''),
                output_field=CharField()
            ),
            V(' '),
            'entity__nombre',
            V(' - '),
            'sucursal__nombre',
        )
    ).all()

    serializer_class = HierarchySerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = HierarchyFilter

    def paginate_queryset(self, queryset):
        if 'no_page' in self.request.query_params:
            return None

        return super().paginate_queryset(queryset)
