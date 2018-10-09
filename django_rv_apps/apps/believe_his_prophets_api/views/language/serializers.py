from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'
