# from rest_framework import serializers
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import list_route
# from rest_framework.exceptions import ParseError
# from django_rv_apps.apps.believe_his_prophets.models.application import Application
# from django_rv_apps.apps.believe_his_prophets.models.language import Language
# from django_rv_apps.apps.believe_his_prophets_api.views.language_view import LanguageSerializer
#
# from django_filters import rest_framework as django_filters
# from rest_framework import filters
# from datetime import datetime
#
# class ApplicationSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Application
#         fields=('id','version','language',
#         'content')
#
# class ApplicationViewSet(viewsets.ModelViewSet):
#     queryset = Application.objects.all().prefetch_related('book','language')
#     serializer_class = ApplicationSerializer
#     filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend,)
#     filter_fields = ('id','version','content')
#     search_fields = ('version',)
#
#
#     @list_route(url_path='reading')
#     def list_reading_Application(self, request):
#         # Declarando variables e instanciando
#         language=''
#         # Obteniendo idioma
#         param_language=request.query_params.get('language','')
#         queryset_language = Language.objects.get(code_iso=param_language)
#         serializer_language= LanguageSerializer(queryset_language,
#                                     many=False)
#         obj_language=serializer_language.data
#
#         reading=BibleRead.objects.filter(
#                         start_date=datenow).values()
#
#         if obj_language:
#             # Get de Application
#             queryset = Application.objects.filter(
#                             version=reading[0]['start_chapter'],
#                             language=obj_language['id'])
#             serializer = ApplicationSerializer(queryset, many=True)
#             obj_reading=serializer.data
#             # Get de Book
#             queryset = Book.objects.get(id=reading[0]['book_id'])
#             serializer_book= BookSerializer(queryset,many=False)
#             obj_book=serializer_book.data
#             # Build de Header
#             obj_header={
#                 'book_name': obj_book['translate_name'],
#                 'chapter':str(reading[0]['start_chapter'])
#             }
#
#         content={
#             'obj_reading': obj_reading,
#             #'obj_book': obj_book,
#             'obj_header': obj_header,
#             'obj_language':obj_language
#         }
#         return Response(content)
