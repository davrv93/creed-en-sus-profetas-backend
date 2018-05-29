from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
from django_filters import rest_framework as django_filters
from rest_framework import filters

class SpiritProphecySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpiritProphecy
        fields='__all__'

class SpiritProphecyViewSet(viewsets.ModelViewSet):
    queryset = SpiritProphecy.objects.all()
    serializer_class = SpiritProphecySerializer
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend,)
    filter_fields = ('id','name',)
    search_fields = ('name',)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        except SpiritProphecy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
       return instance.delete()

    @list_route(url_path='destroy', methods=['post'])
    def destroy_multiple(self, request):
        results = self.get_queryset().filter(id__in=request.data['bulk_id'])
        promise_list = []
        for i in results:
            promise = self.perform_destroy(i)
            if promise is not None:
                promise_list.append(str(promise))
        if len(promise_list) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ParseError(', '.join(list(promise_list)))