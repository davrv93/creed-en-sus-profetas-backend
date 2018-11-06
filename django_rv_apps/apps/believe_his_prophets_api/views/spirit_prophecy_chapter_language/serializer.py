from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapterLanguage


class SpiritProphecyChapterLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpiritProphecyChapterLanguage
        fields = '__all__'
