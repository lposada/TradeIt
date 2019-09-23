from django.urls import path
from . import views as coreviews

urlpatterns = [
    path('', coreviews.home, name="home"),
    path('about/', coreviews.about, name="about"),
    path('store/', coreviews.store, name="store"),
]