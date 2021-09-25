from django.forms import ModelForm
from articleapp import models


class ArticleCreationForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "image", "content"]
