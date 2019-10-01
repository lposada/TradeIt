from django.urls import path
from . import views as views
from .views import ListPost, ListCategory, DetailPost, CrearPost

posts_patterns = ([
    path('', ListCategory.as_view(), name="posts"),
    path('<int:pk>/<slug:slug>/', DetailPost.as_view(), name="post"),
    path('crear/', CrearPost.as_view(), name="crear")
], 'posts')