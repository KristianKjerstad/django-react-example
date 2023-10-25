from django.urls import path

from .views import get, get_all

urlpatterns = [
    path("", get_all, name="get_all"),
    path("<int:id>/", get, name="get_one"),
]
