"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from inicio.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio"),
    path('sobremi',sobremi,name="sobremi"),
    path("registrarse",view_registrarse),
    path("success/",success),
    path("iniciar_sesion",view_iniciar_sesion),
    path("cerrar_sesion",view_cerrar_sesion,name="cerrar_sesion"),
    path("miperfil",view_bio_avatar,name="miperfil"),
    path("resultados",view_userprofilesearch,name="resultados"),
    path("blog",view_blogandlikes,name="blog"),  
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('profile/<str:username>/',profile_detail, name='profile_detail'),
    path('mensajes', view_mensajes, name='mensajes'),
    path('mensajes/inbox', inbox, name='inbox'),
    path('mensajes/send_message/<str:recipient_username>', send_message, name='send_message'),
    path('mensajes/select-recipient', select_recipient, name='select_recipient'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
