from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import AutorSerializer, FraseSerializer
from autores.models import Autor
from frases.models import Frases

# Create your views here.

class AutorListAPIView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    
class AutorCreateAPIView(CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    
class AutorRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    

class FraseListCreateAPIView(ListCreateAPIView):
    queryset = Frases.objects.all()
    serializer_class = FraseSerializer
    
    
class FraseRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Frases.objects.all()
    serializer_class = FraseSerializer

