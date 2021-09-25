from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # 👈 Medial Url 관련
from django.conf import settings  # 👈 Medial Url 관련

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accountapp.urls", namespace="accountapp")),
    path("profiles/", include("profileapp.urls", namespace="profileapp")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
