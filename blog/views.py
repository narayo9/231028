from django.views.generic import ListView, DetailView, CreateView

from blog.forms import PostForm
from blog.models import Post
from django.http import HttpResponseRedirect


class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        return HttpResponseRedirect(self.get_success_url())
