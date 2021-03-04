from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('accounts.urls')),
    url(r'^', include('topic.urls')),
    url(r'^', include('post.urls')),
    url(r'^', include('comments.urls')),

]
