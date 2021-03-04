from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers

from comments.views import CommentsList
from .views import PostList

app_name = "post"

router = routers.SimpleRouter()
router.register(r'post', PostList)


urlpatterns = [
    url(r'^', include(router.urls)),

]
