import unicodedata

from datetime import datetime


from rest_framework import filters, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_rv_apps.apps.believe_his_prophets.models.bible_read import \
    BibleRead
from django_rv_apps.apps.believe_his_prophets.models.book import Book


class PictureMixin(object):

    @action(url_path='picture', methods=['POST'], detail=False)
    def picture(self, request):

        from PIL import Image, ImageDraw, ImageFont
        import uuid
        import textwrap

        lecture = self.request.data.get('lecture')

        if lecture:

            book = lecture.get('book')
            chapter = lecture.get('chapter')
            verses = lecture.get('verses')

            text_from_client = ''

            for x in verses:
                text_from_client += str(x.get('verse')) + \
                    '.'+x.get('data') + "\n"

            maximum = max(verses, key=lambda x: x['verse'])
            minimum = min(verses, key=lambda x: x['verse'])

            text_from_client += book + ' ' + \
                str(chapter) + ': ' + str(minimum.get('verse')) + \
                ' - ' + str(maximum.get('verse'))

            text = textwrap.fill(text_from_client, 50)

            fontcolor = (255, 255, 255)
            fontsize = 40
            font = ImageFont.truetype(
                "/Library/Fonts/Arial.ttf", fontsize)

            img = Image.new("RGBA", (1, 1))
            draw = ImageDraw.Draw(img)
            textsize = draw.textsize(text, font)

            w, h = textsize

            width = w + round(w*0.2)

            height = h + round(h*0.2)

            new_texsize = (width, height)

            background = (145, 146, 215)
            img = Image.new("RGBA", new_texsize, background)
            draw = ImageDraw.Draw(img)
            draw.text(((width - w)/2, (height - h)/2),
                      text, fontcolor, font)

            name = str(uuid.uuid1())+'.png'
            # img.save(name)

            import base64
            from io import BytesIO

            buffered = BytesIO()
            img.save(buffered, format="PNG")

            buffered.seek(0)
            img_bytes = buffered.read()

            base64_encoded_result_bytes = base64.b64encode(img_bytes)
            img_base64_str = base64_encoded_result_bytes.decode('ascii')

            retorno = dict(
                name=name,
                img_base64=img_base64_str
            )

            return Response(retorno)
        else:
            return Response(retorno)
