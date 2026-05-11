from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_page, name="register_page"),
    path("register-user/", views.register_user, name="register_user"),
]

