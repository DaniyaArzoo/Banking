from django.urls import path
from profiles import views

urlpatterns = [
    path("signup/", views.register, name="signup"),
]
