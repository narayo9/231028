from django.views.generic import ListView, DetailView, CreateView

from blog.forms import PostForm
from blog.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostListView(ListView):
    template_name = "post_list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post
