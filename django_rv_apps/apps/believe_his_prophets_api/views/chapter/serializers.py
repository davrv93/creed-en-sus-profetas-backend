from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = '__all__'

