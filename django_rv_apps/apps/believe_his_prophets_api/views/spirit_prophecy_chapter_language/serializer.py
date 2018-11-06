from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_chapter import SpiritProphecyChapterLanguage
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy, SpiritProphecyLanguage


class SpiritProphecyChapterLanguageSerializer(serializers.ModelSerializer):
    book_name = serializers.SerializerMethodField()

    class Meta:
        model = SpiritProphecyChapterLanguage
        fields = '__all__'

    def get_book_name(self, obj):
        request = self.context['request']
        code_iso = request.query_params.get('code_iso')

        instance = SpiritProphecyLanguage.objects.filter(
            language__code_iso=code_iso).first()
        if instance:
            return instance.name
        else:
            return ''
