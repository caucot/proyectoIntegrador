from django.shortcuts import get_list_or_404, render
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Frases
from frases.models import Autor
# Create your views here.

class FrasesListView(ListView):
    model = Frases
    template_name = 'app_frases/listar_frases.html'
    context_object_name = 'listar_frases'    

    def get_queryset(self):
        frases_total = Frases.objects.all()
        autor_pk = self.kwargs.get("autor")  # Obtiene el parámetro desde la URL
        if autor_pk:
            frases_total = frases_total.filter(autor__id=autor_pk)
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
    model = Frases
    fields = ["frase","comentario","fecha_frase"] #Campos a llenar
    template_name = 'crear.html'
    success_url = reverse_lazy('frases:listar_frases')

    

class FrasesUpdateView(UpdateView):
    model = Frases
    fields = '__all__' #
    template_name = 'crear.html'
    success_url = reverse_lazy('frases:listar_frases')
    
    def get_queryset(self): #Metodo para recibir un parametro desde la url, va html
        # Obtenemos un queryset filtrado por la pk desde la URL
        return Frases.objects.filter(pk=self.kwargs.get("pk"))


class FrasesDeleteView(DeleteView):
    model = Frases
    template_name = 'frases/borrar_frases.html'
    success_url = reverse_lazy('frases:listar_frases')
    

def listar_frases_json(request):
    frases = get_list_or_404(Frases, visible = True)
    frases_json = serializers.serialize('json', frases)
    return JsonResponse(frases_json, safe=False)