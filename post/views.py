from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer


class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        topic_slug = self.kwargs.get('topic_slug')

        return queryset.filter(topic__slug=topic_slug)
