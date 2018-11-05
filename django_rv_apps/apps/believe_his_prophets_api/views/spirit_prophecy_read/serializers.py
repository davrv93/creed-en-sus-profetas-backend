from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy_read import SpiritProphecyRead


class SpiritProphecyReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpiritProphecyRead
        fields = '__all__'
