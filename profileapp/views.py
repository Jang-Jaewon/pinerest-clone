from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from . import models
from . import forms
from django.utils.decorators import method_decorator
from profileapp.decorators import profile_ownership_required

# Create your views here.
class ProfileCreateView(CreateView):
    model = models.Profile
    form_class = forms.ProfileCreationForm
    context_object_name = "target_profile"
    # success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    # # success_url 대체
    def get_success_url(self):
        return reverse(
            "accountapp:detail", kwargs={"pk": self.object.user.pk}
        )  # 👈 self.object == Profile


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdateView(UpdateView):
    model = models.Profile
    form_class = forms.ProfileCreationForm
    context_object_name = "target_profile"
    template_name = "profileapp/update.html"

    def get_success_url(self):
        return reverse(
            "accountapp:detail", kwargs={"pk": self.object.user.pk}
        )  # 👈 self.object == Profile
