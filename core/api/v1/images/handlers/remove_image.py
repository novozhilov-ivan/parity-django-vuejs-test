from rest_framework import generics

from core.api.v1.images.serializers import ImagesSerializer
from core.apps.images.models import Images


class DeleteImageAPIView(generics.ListCreateAPIView):
    serializer_class = ImagesSerializer

    # TODO получение списка изображений, добавление, удаление по id
    # queryset = Images.objects.all()