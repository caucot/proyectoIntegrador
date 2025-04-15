from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import AutorSerializer
from autores.models import Autor

# Create your views here.

class AutorListAPIView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    

class AutorRetrieveAPIView(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
