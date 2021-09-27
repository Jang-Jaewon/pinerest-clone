from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # 👈 Medial Url 관련
from django.conf import settings  # 👈 Medial Url 관련

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accountapp.urls", namespace="accountapp")),
    path("profiles/", include("profileapp.urls", namespace="profileapp")),
    path("articles/", include("articleapp.urls", namespace="articleapp")),
    path("comments/", include("commentapp.urls", namespace="commentapp")),
    path("projects/", include("projectapp.urls", namespace="projectapp")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
