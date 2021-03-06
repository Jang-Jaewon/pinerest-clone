from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.models import User
from articleapp import models as articleappModels
from . import forms

has_ownership = [login_required, account_ownership_required]

# Create your views here.
@login_required
def hello_world(request):

    if request.user.is_authenticated:
        return render(request, "accountapp/hello_world.html")
    else:
        return HttpResponseRedirect(reverse("accountapp:login"))


# ํ์๊ฐ์ CBV
class AccountCreateView(CreateView):
    model = User  # ๐ Django์ ๋ด์ฅ๋ User ๋ชจ๋ธ ์ฌ์ฉ
    form_class = UserCreationForm  # ๐ Django์ ๋ด์ฅ๋ Form ์ฌ์ฉ
    success_url = reverse_lazy(
        "accountapp:hello_world"
    )  # ๐ ์ฑ๊ณต ์ ์ด๋ํ  ๊ณณ, ๋ฐ๋์ reverse_lazy
    template_name = "accountapp/create.html"  # ๐ ์๋ ฅ ๋ฐ์ Template


# ๋ก๊ทธ์ธ CBV : settings.py์ "LOGIN_REDIRECT_URL" ์ถ๊ฐ
class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"


# ๋ก๊ทธ์์ CBV : settgins.py์ "LOGOUT_REDIRECT_URL" ์ถ๊ฐ
class AccountLogoutView(LogoutView):
    pass


# ํ๋กํ ๋ณด๊ธฐ CBV
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = articleappModels.Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )


# ํ๋กํ ์์  CBV : AccountCreateView๊ณผ ๊ฑฐ์ ์ ์ฌ
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = User  # ๐ Django์ ๋ด์ฅ๋ User ๋ชจ๋ธ ์ฌ์ฉ
    context_object_name = "target_user"
    form_class = forms.AccountUpdateForm  # ๐ UserCreationForm ์์ ํ usernameํ๋ disabled
    success_url = reverse_lazy(
        "accountapp:hello_world"
    )  # ๐ ์ฑ๊ณต ์ ์ด๋ํ  ๊ณณ, ๋ฐ๋์ reverse_lazy
    template_name = "accountapp/update.html"  # ๐ ์์  ์์ Template


# @login_required
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = User  # ๐ Django์ ๋ด์ฅ๋ User ๋ชจ๋ธ ์ฌ์ฉ
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")  # ๐ ์ฑ๊ณต ์, ์ด๋ํ  ๊ณณ
    template_name = "accountapp/delete.html"  # ๐ ์ญ์  ํ์ด์ง
