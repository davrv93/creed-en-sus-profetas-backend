from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.file import File


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ('id','book','language',
        'chapter','commentary_html','commentary',
        'commentary_file','commentary_url')


class AudioSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    class Meta:
        model = Chapter
        fields = ('id','url')

    def get_url(self,obj):

        if obj.audio:

            return obj.audio.url

        else:

            return None

class FileSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','url')

    def get_url(self,obj):

        if obj.audio:

            return obj.audio.url

        else:

            return None



