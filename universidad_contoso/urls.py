from django.contrib import admin
from django.urls import path
from gestion_academica.views import lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cursos/', lista_cursos),  # Nueva API para cursos
]
