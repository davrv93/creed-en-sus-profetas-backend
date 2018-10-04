
from django.db import models
from .book import Book

class BibleRead(models.Model):
    id = models.AutoField(
         primary_key=True,
         editable=False)
    start_date = models.DateField(
        blank=False, null=False
        )
    book = models.ForeignKey(
        Book, db_column='book_id',
        blank=False, null=False,
        on_delete=models.PROTECT)
    start_chapter = models.IntegerField(
        blank=False, null=False)
    end_chapter = models.IntegerField(
        blank=False, null=False)

    class Meta:
        verbose_name = 'BibleRead'
        db_table = 'bible_read'
        verbose_name_plural = 'BibleRead'


    def __str__(self):
        return (self.book.__str__() +
                str(self.start_chapter))
