from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.exceptions import ParseError
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets.models.book import Book
from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter


class VerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields=('id','book','language',
        'chapter','verse','data','highlight')

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields=('id','name','translate_name','testament',)

class ChapterSerializer(serializers.ModelSerializer):

    commentary_append = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields='__all__'

    def get_commentary_append(self,obj):
        if obj.commentary_file:
            import urllib2
            from BeautifulSoup import BeautifulSoup
            url='https://davrv93.pythonanywhere.com'+obj.commentary_file.url
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)

            x = soup.body.find('div', attrs={'class' : 'container'}).text
            return x
        else:
            return None
