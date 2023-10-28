from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostForm, CommentForm
from blog.models import Post
from django.urls import reverse_lazy


class PostCreateView(LoginRequiredMixin, CreateView):
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

    def get_comment_form(self):
        return CommentForm(self.request.POST or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = (
            kwargs.get("form") if kwargs.get("form") else self.get_comment_form()
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_comment_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.created_by = request.user
            comment.save()
        return self.render_to_response(self.get_context_data(form=form))
