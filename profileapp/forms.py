from django.db.models import fields
from django.forms import ModelForm
from . import models


class ProfileCreationForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ["image", "nickname", "message"]
