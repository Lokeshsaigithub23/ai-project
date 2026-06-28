from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("preview/", views.preview, name="preview"),

    # MongoDB Media
    path("media/<str:file_id>/", views.serve_media, name="serve_media"),
]