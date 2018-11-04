from rest_framework import serializers
from django_rv_apps.apps.believe_his_prophets.models.hierarchy import Hierarchy


class HierarchySerializer(serializers.ModelSerializer):

    # nombre = serializers.SerializerMethodField()

    nombre = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Hierarchy
        fields = '__all__'

    # def get_nombre(self, obj):
    #     sucursal = ''

    #     hierarchy_type = ''

    #     entidad = ''

    #     nombre = ''

    #     connector = ''

    #     if obj.sucursal:

    #         sucursal = obj.sucursal.nombre

    #     if obj.entity:

    #         entidad = obj.entity.nombre

    #         if obj.entity.hierarchy_type:

    #             hierarchy_type = obj.entity.hierarchy_type.name

    #             if obj.entity.hierarchy_type.connector:

    #                 connector = obj.entity.hierarchy_type.connector

    #             hierarchy_type + ' ' + connector

    #     nombre = hierarchy_type + entidad + ' - ' + sucursal

    #     return nombre
