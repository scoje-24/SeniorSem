# museums/urls.py

from django.urls import path
from museums import views

urlpatterns = [
    path("", views.museum_index, name="museum_index"),
    path("<int:pk>/", views.museum_detail, name="museum_detail"),
]
