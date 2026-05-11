
from django.urls import path
from . import views
from .views import lost_and_found, admin_dashboard, know_your_teacher

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    
    # Login / Register
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("register-user/", views.register_user, name="register_user"),
    
    # Complaint
    path("complaint/", views.complaint, name="complaint"),
    path("complaint/success/", views.complaint_success, name="complaint_success"),
    
    # Lost and Found
    path("lost-found/", lost_and_found, name="lost_found"),
    
    # Admin
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    
    # Know your teacher
    path("know-your-teacher/", know_your_teacher, name="know_teacher"),
]
