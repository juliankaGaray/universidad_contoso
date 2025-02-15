from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usuario, Estudiante, Profesor, Departamento, Curso, Inscripcion, Evaluacion, HistorialAcademico
from .serializers import UsuarioSerializer, EstudianteSerializer, ProfesorSerializer, DepartamentoSerializer, CursoSerializer, InscripcionSerializer, EvaluacionSerializer, HistorialAcademicoSerializer

def home_view(request):
    return render(request, 'home.html')

# Vistas para Usuario
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vistas para Estudiante
class EstudianteListCreateView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Nueva vista para mostrar el formulario de estudiantes
def estudiante_create_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')

        if nombre and apellido and correo:
            Estudiante.objects.create(nombre=nombre, apellido=apellido, correo=correo)
            return redirect('estudiante-list')  # Redirige a la lista de estudiantes

    return render(request, 'estudiante.html')

# Vistas para Profesor
class ProfesorListCreateView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ProfesorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

# Vistas para Departamento
class DepartamentoListCreateView(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

# Vistas para Curso
class CursoListCreateView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Vistas para Inscripcion
class InscripcionListCreateView(generics.ListCreateAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class InscripcionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

# Vistas para Evaluacion
class EvaluacionListCreateView(generics.ListCreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class EvaluacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

# Vistas para Historial Academico
class HistorialAcademicoListCreateView(generics.ListCreateAPIView):
    queryset = HistorialAcademico.objects.all()
    serializer_class = HistorialAcademicoSerializer

class HistorialAcademicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialAcademico.objects.all()
    serializer_class = HistorialAcademicoSerializer
