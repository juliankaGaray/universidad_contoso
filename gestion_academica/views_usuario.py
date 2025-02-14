# Vistas para Usuario
from gestion_academica.models import Usuario
from gestion_academica.serializers import UsuarioSerializer


from rest_framework import generics


class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer