from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from comments.views import CommentsList
from post.views import PostList
from .views import TopicList

app_name = "topic"

router = routers.SimpleRouter()
router.register(r'topic', TopicList)
topic_router = routers.NestedSimpleRouter(router, r'topic', lookup='topic')
topic_router.register(r'post', PostList, basename='post')
topic_router.register(r'comments', CommentsList, basename='comments')
post_router = routers.NestedSimpleRouter(topic_router, r'post', lookup='post')
post_router.register(r'comments', CommentsList, basename='comments')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(post_router.urls)),
]
