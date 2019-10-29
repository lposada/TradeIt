"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from usuarios.urls import usuarios_patterns
from libros.urls import libros_patterns
from posts.urls import posts_patterns
from trueque.urls import trueque_patterns

urlpatterns = [
    path('', include('core.urls')),
    #Admins
    path('services/', include ('services.urls')),
    path('page/', include ('pages.urls')),
    path('contact/', include ('contact.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('posts/', include (posts_patterns)),
    path('usuarios/', include (usuarios_patterns)),
    path('libros/', include (libros_patterns)),
    path('trueque/',  include(trueque_patterns)),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)