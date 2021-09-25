from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from . import models
from . import forms


# Create your views here.
class ProfileCreateView(CreateView):
    models = models.Profile
    form_class = forms.ProfileCreationForm
    context_object_name = "target_profile"
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
