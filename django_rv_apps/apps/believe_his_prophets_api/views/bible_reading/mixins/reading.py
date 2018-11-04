import unicodedata

from datetime import datetime


from rest_framework import filters, serializers, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from django_rv_apps.apps.believe_his_prophets.models.bible_read import \
    BibleRead
from django_rv_apps.apps.believe_his_prophets.models.book import Book

from django_rv_apps.apps.believe_his_prophets.models.chapter import Chapter
from django_rv_apps.apps.believe_his_prophets.models.verse import Verse
from django_rv_apps.apps.believe_his_prophets_api.views.bible_reading.serializers import (BookSerializer,
                                                                                          VerseSerializer,
                                                                                          ChapterSerializer,
                                                                                          BibleReadSerializer)


class ReadingMixin(object):

    @list_route(url_path='reading')
    def list_reading_verse(self, request):
        # Declarando variables e instanciando
        def remove_accents(data):
            return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')

        reading = {}
        book = {}
        chapter = {}
        retorno = {}

        # Obteniendo fecha por defecto
        p_date = request.query_params.get('date', None)
        i = datetime.now()
        datenow = i.strftime('%Y-%m-%d')

        if p_date:
            datenow = p_date
            print('p_date', datenow)

        # Obteniendo idioma
        language = request.query_params.get('language', 'ES')

        reading = BibleRead.objects.filter(start_date=datenow).first()

        if reading:
            # Get de Verse
            queryset = Verse.objects.filter(
                book=reading.book_id,
                chapter=reading.start_chapter,
                language__code_iso=language)

            serializer = VerseSerializer(queryset, many=True)
            verse = serializer.data

            retorno['for_audio'] = ' '.join([x['data'] for x in verse])
            from PIL import Image, ImageDraw, ImageFont

            for x in verse:
                x['data_clean'] = remove_accents(x['data'])

                # img = Image.new('RGB', (400, 400), color=(73, 109, 137))

                # fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
                # d = ImageDraw.Draw(img)
                # d.text((10, 10), x['data'], font=fnt, fill=(255, 255, 0))

                # img.save(str(x['chapter'])+str(x['verse'])+'.png')

                from PIL import ImageFont, Image, ImageDraw
                import textwrap

                # Source text, and wrap it.
                userinput = x['data']
                text = textwrap.fill(userinput, 50)

                # Font size, color and type.
                fontcolor = (255, 255, 255)
                fontsize = 40
                font = ImageFont.truetype(
                    "/Library/Fonts/Arial.ttf", fontsize)

                # Determine text size using a scratch image.
                img = Image.new("RGBA", (1, 1))
                draw = ImageDraw.Draw(img)
                textsize = draw.textsize(text, font)

                w, h = textsize

                width = w + round(w*0.2)

                height = h + round(h*0.2)

                new_texsize = (width, height)

                print('w', w)

                print('h', h)

                # Now that we know how big it should be, create
                # the final image and put the text on it.
                background = (145, 146, 215)
                img = Image.new("RGBA", new_texsize, background)
                draw = ImageDraw.Draw(img)
                draw.text(((width - w)/2, (height - h)/2),
                          text, fontcolor, font)

                # img.show()
                img.save(str(x['chapter'])+str(x['verse'])+'.png')

            from gtts import gTTS
            import os
            import requests

            from requests.packages.urllib3.exceptions import InsecureRequestWarning

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

            # tts = gTTS(text=retorno['for_audio'], lang='es')
            # tts.save("good.mp3")

            retorno['verse'] = verse

            # Get de Book
            queryset = Book.objects.filter(id=reading.book_id).first()

            serializer = BookSerializer(queryset)
            book = serializer.data
            retorno['book'] = book

            # Get de Chapter
            queryset = Chapter.objects.filter(
                book_id=reading.book_id,
                chapter=reading.start_chapter,
                language__code_iso=language).first()

            serializer = ChapterSerializer(queryset)
            chapter = serializer.data
            retorno['chapter'] = chapter

        return Response(retorno)
