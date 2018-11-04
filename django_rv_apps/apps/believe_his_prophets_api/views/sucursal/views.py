from django_filters import rest_framework as django_filters

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import permissions

from django_rv_apps.apps.believe_his_prophets.models.sucursal import Sucursal

from .serializer import SucursalSerializer


from .filters import SucursalFilter


class SucursalCreateView(ListCreateAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = SucursalFilter


class SucursalDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = SucursalFilter

    # permission_classes = (permissions.IsAuthenticated,)

    def paginate_queryset(self, queryset):
        return None
