"""universidad_contoso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path
from gestion_academica import views
from gestion_academica.views_usuario import UsuarioListCreateView
from django.http import HttpResponse
from gestion_academica.views import estudiante_create_view

def home_redirect(request):
    return redirect('usuario-list')  # Redirige a la vista de lista de usuarios
    


urlpatterns = [
    path('', views.home_view, name='home'),
    path('usuarios/', views.UsuarioListCreateView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('estudiantes/nuevo/', estudiante_create_view, name='estudiante-create'),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('profesores/', views.ProfesorListCreateView.as_view(), name='profesor-list'),
    path('profesores/<int:pk>/', views.ProfesorDetailView.as_view(), name='profesor-detail'),
    path('departamentos/', views.DepartamentoListCreateView.as_view(), name='departamento-list'),
    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='departamento-detail'),
    path('cursos/', views.CursoListCreateView.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso-detail'),
    path('inscripciones/', views.InscripcionListCreateView.as_view(), name='inscripcion-list'),
    path('inscripciones/<int:pk>/', views.InscripcionDetailView.as_view(), name='inscripcion-detail'),
    path('evaluaciones/', views.EvaluacionListCreateView.as_view(), name='evaluacion-list'),
    path('evaluaciones/<int:pk>/', views.EvaluacionDetailView.as_view(), name='evaluacion-detail'),
    path('historial/', views.HistorialAcademicoListCreateView.as_view(), name='historial-list'),
    path('historial/<int:pk>/', views.HistorialAcademicoDetailView.as_view(), name='historial-detail'),
]

