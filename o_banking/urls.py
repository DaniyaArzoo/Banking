from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from finance.views import passbook

urlpatterns = [
    path("admin/", admin.site.urls),
    path("finance/", include("finance.urls")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profiles/", include("profiles.urls")),
    path("", passbook),
]
