from django.urls import path

from blog.views import PostCreateView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
]
