
# from django.db import models
# from django.db.models.deletion import ProtectedError
# from django_rv_apps.apps.believe_his_prophets.models.spirit_prophecy import SpiritProphecy
# from django_rv_apps.apps.believe_his_prophets.models.language import Language

# class SpiritProphecyTitle(models.Model):
#     id = models.AutoField(
#          primary_key=True,
#          editable=False)
#     name = models.CharField(
#         max_length=30,
#         blank=False, null=False)
#     spirit_prophecy = models.ForeignKey(
#         SpiritProphecy,
#         db_column='spirit_prophecy_id',
#         blank=False, null=False)
#     language = models.ForeignKey(
#         Language, db_column='language_id',
#         blank=True, null=True)


#     class Meta:
#         verbose_name = 'SpiritProphecyTitle'
#         db_table = 'believe_spirit_prophecy_title'
#         verbose_name_plural = 'SpiritProphecyTitle'
#         default_permissions = ()
#         permissions = (
#             ('add_spiritprophecytitle',
#              'Puede agregar SpiritProphecyTitle'),
#             ('change_spiritprophecytitle',
#              'Puede actualizar SpiritProphecyTitle'),
#             ('delete_spiritprophecytitle',
#              'Puede eliminar SpiritProphecyTitle'),
#             ('list_spiritprophecytitle',
#              'Puede listar SpiritProphecyTitle'),
#             ('get_spiritprophecytitle',
#              'Puede obtener SpiritProphecyTitle'),
#             ('listform_spiritprophecytitle',
#               'Puede listar SpiritProphecyTitle en Formularios'),
#         )

#     def __str__(self):
#         return (self.name)

#     def delete(self, *args, **kwargs):
#         try:
#             super(SpiritProphecyTitle, self).delete(*args, **kwargs)
#         except ProtectedError as e:
#             return (self.name)