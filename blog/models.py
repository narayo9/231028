from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "글"
        verbose_name_plural = "글 목록"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"