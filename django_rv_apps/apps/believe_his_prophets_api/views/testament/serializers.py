from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.testament import Testament


class TestamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testament
        fields = '__all__'
