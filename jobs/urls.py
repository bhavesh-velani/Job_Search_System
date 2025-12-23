
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.job_search, name="job_search"),
]
