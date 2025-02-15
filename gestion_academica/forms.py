from django import forms
from .models import Estudiante, Curso, Profesor, Inscripcion, Departamento, Evaluacion, HistorialAcademico

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'telefono', 'fecha_inscripcion']
        # Opcional: personalizar los widgets y etiquetas
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'creditos', 'descripcion', 'departamento', 'profesores']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'email', 'telefono', 'especialidad']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['inscripcion', 'tipo', 'nota', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class HistorialAcademicoForm(forms.ModelForm):
    class Meta:
        model = HistorialAcademico
        fields = ['estudiante', 'promedio_general', 'estado']
