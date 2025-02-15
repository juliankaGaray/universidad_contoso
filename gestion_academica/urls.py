from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Rutas para Estudiantes
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/<int:estudiante_id>/editar/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/<int:estudiante_id>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
    
    # Rutas para Cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/<int:curso_id>/editar/', views.editar_curso, name='editar_curso'),
    path('cursos/<int:curso_id>/eliminar/', views.eliminar_curso, name='eliminar_curso'),
    
    # Rutas para Departamentos (ya definidas anteriormente)
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
    path('departamentos/<int:departamento_id>/editar/', views.editar_departamento, name='editar_departamento'),
    path('departamentos/<int:departamento_id>/eliminar/', views.eliminar_departamento, name='eliminar_departamento'),
    
    # Rutas para Profesores (nuevas)
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesores/<int:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
    path('profesores/crear/', views.crear_profesor, name='crear_profesor'),
    path('profesores/<int:profesor_id>/editar/', views.editar_profesor, name='editar_profesor'),
    path('profesores/<int:profesor_id>/eliminar/', views.eliminar_profesor, name='eliminar_profesor'),
]
