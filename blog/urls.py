from django.urls import path

from blog.views import PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/', PostListView.as_view(), name='post_list'),
]
