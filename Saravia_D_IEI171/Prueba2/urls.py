"""
URL configuration for Prueba2 project.

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
from django.urls import path
from prueba_App import views as p

urlpatterns = [
    path('', p.RenderIndex),
    path('socios/', p.ListarSocios),
    path('agregar/', p.AgregarSocio),
    path('eliminar/<int:id>', p.EliminarSocio),
    path('editar/<int:id>', p.EditarSocio)
]
