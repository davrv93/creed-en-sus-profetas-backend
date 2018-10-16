from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.application import Application
from django_rv_apps.apps.believe_his_prophets.models.language import Language
# from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer
# test
from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'version', 'language', 'code',
                  'content')


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().prefetch_related('language')
    serializer_class = ApplicationSerializer
    filter_backends = (filters.SearchFilter,
                       django_filters.DjangoFilterBackend,)
    filter_fields = ('id', 'version', 'content')
    search_fields = ('version',)

    @list_route(url_path='status')
    def list_status(self, request):
        # Declarando variables e instanciando
        obj_response = {}
        language = ''
        # Obteniendo idioma
        param_language = request.query_params.get('language', '')
        param_version = request.query_params.get('version', '')
        print('param_language status', param_language)
        print('param_version status', param_version)
        if param_language:
            queryset_language = Language.objects.get(code_iso=param_language)
            serializer_language = LanguageSerializer(queryset_language,
                                                     many=False)
            obj_language = serializer_language.data
            print('obj_language', obj_language)

            if obj_language:
                # Get de Application
                queryset = Application.objects.filter(
                    language__code_iso=param_language,
                    is_active='1'
                )
                if queryset:
                    serializer = ApplicationSerializer(queryset, many=True)
                    obj_version = serializer.data
                    print('obj_version ', obj_version[0])
                    if obj_version:
                        obj_response = {
                            'version': obj_version[0]['version'],
                            'content': obj_version[0]['content'],
                            'code': obj_version[0]['code'],
                            'condition': True
                        }
                        print('obj_response 1', obj_response)

                    else:
                        obj_response = {
                            'condition': False
                        }
                        print('obj_response 2', obj_response)
                else:
                    obj_response = {
                        'condition': False
                    }
                    print('obj_response 3', obj_response)
        else:
            obj_response = {
                'condition': False
            }
            print('obj_response 4', obj_response)
        print('obj_response 5 ', obj_response)

        return Response(obj_response)
