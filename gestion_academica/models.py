from django.db import models

# Clase base abstracta para compartir campos comunes
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True

# Estudiante hereda de Usuario
class Estudiante(Usuario):
    fecha_inscripcion = models.DateField()

# Profesor hereda de Usuario
class Profesor(Usuario):
    especialidad = models.CharField(max_length=100)

# Departamento académico
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

# Curso asociado a un Departamento
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    creditos = models.IntegerField()
    descripcion = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='cursos')
    profesores = models.ManyToManyField(Profesor, related_name='cursos')  # Relación muchos a muchos
    
    def __str__(self):
        return self.titulo

# Inscripción de un Estudiante en un Curso
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField()
    
    def __str__(self):
        return f"{self.estudiante} en {self.curso}"

# Evaluación asociada a una Inscripción
class Evaluacion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name='evaluaciones')
    tipo = models.CharField(max_length=50)  # Ej: Parcial, Final, Tarea
    nota = models.FloatField()
    fecha = models.DateField()
    
    def __str__(self):
        return f"{self.tipo} - {self.nota}"

# Historial Académico del Estudiante
class HistorialAcademico(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='historial')
    promedio_general = models.FloatField()
    estado = models.CharField(max_length=50)  # Ej: Activo, Graduado, Suspendido
    
    def __str__(self):
        return f"Historial de {self.estudiante}"
