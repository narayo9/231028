from django.urls import path

from blog.views import PostCreateView, PostListView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/', PostListView.as_view(), name='post_list'),
]
