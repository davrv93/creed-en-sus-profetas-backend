from rest_framework import serializers

from django_rv_apps.apps.believe_his_prophets.models.book import Book, BookLanguage


class BookSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_name(self,obj):

        code_iso = self.context.get('code_iso')

        print('code_iso',code_iso)

        book_language = BookLanguage.objects.get(
            book=obj.id,
            language__code_iso=code_iso
        )

        if book_language:

            return book_language.name

        else:

            return ''


