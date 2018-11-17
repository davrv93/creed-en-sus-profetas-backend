from rest_framework.response import Response

from rest_framework.decorators import action

from django_rv_apps.apps.believe_his_prophets.models.chapter import  Chapter

class AudioMixin(object):

    @action(url_path='audio', methods=['GET'], detail=True)
    def audio(self, request, pk=None):

        instance = self.get_queryset().get(pk=pk)
        retorno = dict()

        if instance.audio:
            retorno.update(
                url=instance.audio.url
            )
        else:
            retorno.update(
                url=None
            )
        return Response(data=retorno)