from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Curso
from .serializers import CursoSerializer

@api_view(['GET', 'POST'])
def lista_cursos(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
