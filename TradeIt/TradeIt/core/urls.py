from django.urls import path
from . import views as coreviews

urlpatterns = [
    path('', coreviews.home, name="home"),
]