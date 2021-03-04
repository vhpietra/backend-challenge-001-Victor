from .models import Comments
from rest_framework import viewsets
from .serializers import CommentsSerializer


class CommentsList(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

