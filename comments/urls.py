from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers
from .views import CommentsList

app_name = "comments"

router = routers.SimpleRouter()
router.register(r'comments', CommentsList)

urlpatterns = [
    url(r'^', include(router.urls)),
]
