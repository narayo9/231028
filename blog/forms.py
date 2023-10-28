from django.forms import ModelForm

from blog.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["description"]