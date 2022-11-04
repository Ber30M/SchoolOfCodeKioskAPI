from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
]
# go to app/views
