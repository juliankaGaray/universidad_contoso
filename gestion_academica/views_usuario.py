# Vistas para Usuario
from gestion_academica.models import Usuario
from gestion_academica.serializers import UsuarioSerializer


from rest_framework import generics

# vita para Ususario
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer