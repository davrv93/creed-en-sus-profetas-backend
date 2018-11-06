
from django.db import models
from django.db.models.deletion import ProtectedError
from .testament import Testament
from django_rv_apps.apps.believe_his_prophets.models.language import Language


class Book(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    testament = models.ForeignKey(
        Testament, db_column='testament_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ManyToManyField(
        Language,
        through='BookLanguage', blank=True,
        related_name='book_language_set'
    )
    book_order = models.IntegerField(
        blank=False, null=False)

    class Meta:
        verbose_name = 'Book'
        db_table = 'believe_book'
        verbose_name_plural = 'Book'

    def __str__(self):
        return str(self.book_order)


class BookLanguage(models.Model):

    id = models.AutoField(
        primary_key=True,
        editable=False)
    name = models.CharField(
        max_length=100,
        blank=False, null=False)
    abrev = models.CharField(
        max_length=100,
        blank=True, null=True)
    book = models.ForeignKey(
        'Book', db_column='book_id',
        related_name='book_language_book_set',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        Language, db_column='language_id',
        related_name='book_language_language_set',
        blank=False, null=False,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'BookLanguage'
        verbose_name_plural = 'BookLanguage'
        db_table = 'believe_book_language'
