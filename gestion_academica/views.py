from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Curso, HistorialAcademico
from .forms import EstudianteForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm
from .models import Departamento
from .forms import DepartamentoForm
from .models import Profesor
from .forms import ProfesorForm


def home(request):
    """
    Vista principal que muestra un resumen o enlaces a las secciones principales.
    """
    return render(request, 'gestion_academica/home.html')

def base(request):
    """
    Vista principal que muestra un resumen o enlaces a las secciones principales.
    """
    return render(request, 'gestion_academica/base.html')

def lista_estudiantes(request):
    """
    Vista que lista todos los estudiantes.
    """
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion_academica/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    """
    Vista que muestra el detalle de un estudiante en particular, incluyendo su historial académico si existe.
    """
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    
    # Intenta obtener el historial académico del estudiante
    historial = getattr(estudiante, 'historial', None)
    
    return render(request, 'gestion_academica/detalle_estudiante.html', {
        'estudiante': estudiante,
        'historial': historial,
    })

def lista_cursos(request):
    """
    Vista que lista todos los cursos disponibles.
    """
    cursos = Curso.objects.all()
    return render(request, 'gestion_academica/lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    """
    Vista que muestra los detalles de un curso, junto con las inscripciones asociadas.
    """
    curso = get_object_or_404(Curso, id=curso_id)
    # Accedemos a las inscripciones relacionadas con este curso usando el related_name definido en el modelo.
    inscripciones = curso.inscripciones.all()
    
    return render(request, 'gestion_academica/detalle_curso.html', {
        'curso': curso,
        'inscripciones': inscripciones,
    })
    
    #  crear estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'gestion_academica/crear_estudiante.html', {'form': form})

def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('detalle_estudiante', estudiante_id=estudiante.id)
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'gestion_academica/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

#  eliminar  estudiante

def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'gestion_academica/eliminar_estudiante.html', {'estudiante': estudiante})

#  crear curso

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion_academica/crear_curso.html', {'form': form})
#  editar curso 


def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalle_curso', curso_id=curso.id)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'gestion_academica/editar_curso.html', {'form': form, 'curso': curso})
#  eliminar  curso 
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'gestion_academica/eliminar_curso.html', {'curso': curso})

# DEPARTAMENTOS



#listar depto
def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'gestion_academica/lista_departamentos.html', {'departamentos': departamentos})

def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'gestion_academica/crear_departamento.html', {'form': form})

#editar depto

def editar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'gestion_academica/editar_departamento.html', {'form': form, 'departamento': departamento})
#eliminar depto

def eliminar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('lista_departamentos')
    return render(request, 'gestion_academica/eliminar_departamento.html', {'departamento': departamento})

#     PROFEORES


 #listar profesores
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'gestion_academica/lista_profesores.html', {'profesores': profesores})

def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'gestion_academica/detalle_profesor.html', {'profesor': profesor})
 #crear profesor
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'gestion_academica/crear_profesor.html', {'form': form})
#editar profesor
def editar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('detalle_profesor', profesor_id=profesor.id)
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'gestion_academica/editar_profesor.html', {'form': form, 'profesor': profesor})
#eliminar profesor
def eliminar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('lista_profesores')
    return render(request, 'gestion_academica/eliminar_profesor.html', {'profesor': profesor})
