from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import models
from articleapp import models as articleappModels
from projectapp import models as projectappModels


@method_decorator(login_required, "get")
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse(
            "projectapp:detail", kwargs={"pk": self.request.GET.get("project_pk")}
        )

    # 구독 토글 기능
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(
            projectappModels.Project, pk=self.request.GET.get("project_pk")
        )  # 👈 project 정보
        user = self.request.user  # 👈 현재 user
        subcription = models.Subscription.objects.filter(
            user=user, project=project
        )  # 👈 subscription 정보
        if subcription.exists():  # 👈 이미 구독정보가 존재하면 삭제
            subcription.delete()
        else:  # 👈 구독정보가 존재하지않으면 생성
            models.Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, "get")
class SubscriptionListView(ListView):
    model = articleappModels.Article
    context_object_name = "article_list"
    template_name = "subscribeapp/list.html"
    paginate_by = 5

    def get_queryset(self):
        projects = models.Subscription.objects.filter(
            user=self.request.user
        ).values_list(
            "project"
        )  # 👈 구독한 모든 프로젝트
        article_list = articleappModels.Article.objects.filter(
            project__in=projects
        )  # 👈 구독한 모든 프로젝트가 포함된 article
        return article_list
