from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post


class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    fields = ["title", "description", "created_by"]