# project-level urls.py (config/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),          # Admin panel
    path("", include("api.urls")),            # All normal web pages (home, register, complaint, etc.)
    path("api/", include("api.urls")),        # API URLs (login API)
]
