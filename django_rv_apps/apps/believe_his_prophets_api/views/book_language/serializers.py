from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.book_language import BookLanguage


class BookLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookLanguage
        fields = '__all__'
