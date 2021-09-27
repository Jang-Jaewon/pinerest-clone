from django.db import models
from django.contrib.auth.models import User
from projectapp import models as projectModels

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="article", null=True
    )
    project = models.ForeignKey(
        projectModels.Project,
        on_delete=models.SET_NULL,
        null=True,
        related_name="article",
    )
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
