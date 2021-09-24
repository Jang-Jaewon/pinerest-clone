from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import forms


# Create your views here.
def hello_world(request):
    return render(request, "accountapp/hello_world.html")


# 회원가입 CBV
class AccountCreateView(CreateView):
    model = User  # 👈 Django의 내장된 User 모델 사용
    form_class = UserCreationForm  # 👈 Django의 내장된 Form 사용
    success_url = reverse_lazy(
        "accountapp:hello_world"
    )  # 👈 성공 시 이동할 곳, 반드시 reverse_lazy
    template_name = "accountapp/create.html"  # 👈 입력 받을 Template


# 로그인 CBV : settings.py에 "LOGIN_REDIRECT_URL" 추가
class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"


# 로그아웃 CBV : settgins.py에 "LOGOUT_REDIRECT_URL" 추가
class AccountLogoutView(LogoutView):
    pass


# 프로필 보기 CBV
class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"


# 프로필 수정 CBV : AccountCreateView과 거의 유사
class AccountUpdateView(UpdateView):
    model = User  # 👈 Django의 내장된 User 모델 사용
    context_object_name = "target_user"
    form_class = forms.AccountUpdateForm  # 👈 UserCreationForm 상속 후 username필드 disabled
    success_url = reverse_lazy(
        "accountapp:hello_world"
    )  # 👈 성공 시 이동할 곳, 반드시 reverse_lazy
    template_name = "accountapp/update.html"  # 👈 수정 양식 Template


class AccountDeleteView(DeleteView):
    model = User  # 👈 Django의 내장된 User 모델 사용
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")  # 👈 성공 시, 이동할 곳
    template_name = "accountapp/delete.html"  # 👈 삭제 페이지
