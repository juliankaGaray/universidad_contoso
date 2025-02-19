from django import forms
from .models import Estudiante, Curso, Profesor, Inscripcion, Departamento, Evaluacion, HistorialAcademico

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'telefono', 'fecha_inscripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'creditos', 'descripcion', 'departamento', 'profesores']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'profesores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'email', 'telefono', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['inscripcion', 'tipo', 'nota', 'fecha']
        widgets = {
            'inscripcion': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class HistorialAcademicoForm(forms.ModelForm):
    class Meta:
        model = HistorialAcademico
        fields = ['estudiante', 'promedio_general', 'estado']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'promedio_general': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }
