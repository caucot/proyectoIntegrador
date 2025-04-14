from django.shortcuts import get_list_or_404, render
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Frases
from frases.models import Autor
# Create your views here.

class FrasesListView(ListView):
    model = Frases
    template_name = 'app_frases/listar_frases.html'
    context_object_name = 'listar_frases'    

    def get_queryset(self): #Metodo para recibir un parametro desde la url
        frases_total = Frases.objects.all() #Frases_total lista todos los obj por defecto
        autor_id = self.request.GET.get("autor") #Obtiene la variable autor del html, linea 53
        if autor_id: #En caso de recibir un id, entonces filtra frases_total por autor.id
            frases_total = frases_total.filter(autor__nombre=nombre_autor) 
        return frases_total
    
class VisibleListView(ListView):
    queryset = Frases.objects.all().filter(visible=True)
    template_name = 'app_frases/listar_frases.html'
    context_object_name = 'listar_frases'
    
    
class InvisibleListView(ListView):
    queryset = Frases.objects.all().filter(visible=False)
    template_name = 'app_frases/listar_frases.html'
    context_object_name = 'listar_frases'
    
class FrasesCreateView(CreateView):
    frase = Frases
    fields = ["frase","comentario","fecha_frase"] #Campos a llenar
    template_name = 'crear.html'
    success_url = reverse_lazy('frases:listar_frases')
    

class FrasesUpdateView(UpdateView):
    frase = Frases
    fields = '__all__' #
    template_name = 'crear.html'
    success_url = reverse_lazy('frases:listar_frases')


class FrasesDeleteView(DeleteView):
    frase = Frases
    template_name = 'frases/borrar_frases.html'
    success_url = reverse_lazy('frases:listar_frases')
    

def listar_frases_json(request):
    frases = get_list_or_404(Frases, visible = True)
    frases_json = serializers.serialize('json', frases)
    return JsonResponse(frases_json, safe=False)