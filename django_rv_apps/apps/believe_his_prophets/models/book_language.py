
from django.db import models
from .book import Book
from .language import Language

class BookLanguage(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    book = models.ForeignKey(
        Book,
        db_column='book_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    language = models.ForeignKey(
        Language,
        db_column='language_id',
        blank=False, null=False,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        max_length=100,
        blank=False, null=False)
    abreviation = models.CharField(
        max_length=100,
        blank=True, null=True)


    class Meta:
        verbose_name = 'Book language'
        verbose_name_plural = 'Book language'
        db_table = 'believe_book_lang'

    def __str__(self):
        return self.name