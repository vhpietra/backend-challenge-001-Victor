from .models import Topic
from rest_framework import viewsets
from .serializers import TopicSerializer


class TopicList(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'slug'
