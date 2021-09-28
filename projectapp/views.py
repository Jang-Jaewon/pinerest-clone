from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin
from . import forms
from . import models
from articleapp import models as articleappModels
from subscribeapp import models as subscribeappModels
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)


# Create your views here.
@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = models.Project
    from_class = forms.ProjectCreationForm
    template_name = "projectapp/create.html"
    fields = ["image", "title", "description"]

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = models.Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = subscribeappModels.Subscription.objects.filter(
                user=user, project=project
            )
        object_list = articleappModels.Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(
            object_list=object_list, subscription=subscription, **kwargs
        )


class ProjectListView(ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 25
