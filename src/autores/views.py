from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from frases.models import Frases

from .models import Autor
from frases.models import Frases
# Create your views here.

def inicio(request):
    return render(request, 'app_autores/inicio.html')


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request,
                'app_autores/listar.html',
                  {'autores': autores})
    
def autores_activos(request):
    autores = Autor.objects.all().filter(activo=True)
    return render(request,
                'app_autores/listar.html',
                  {'autores': autores})

def autores_inactivos(request):
    autores = Autor.objects.all().filter(activo=False)
    return render(request,
                'app_autores/listar.html',
                  {'autores': autores})

def listar_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    return JsonResponse(autores_json, safe=False)


def detalle_autor(request,id):
    autor  = get_object_or_404(Autor, id = id)
    frases = get_list_or_404(Frases, id= id)
    cant_frases = len(frases)
    return render(request,
                  'app_autores/detalle.html',
                  {'autor': autor,
                   'cantidad_frases': cant_frases}
                  )

def borrar_autor(request, id):
    autor_a_borrar = get_object_or_404(Autor, id=id)
    autor_a_borrar.delete() 
    return HttpResponseRedirect(reverse('autores:listar_autores'))

def estado_autor(request,id):
    autor_a_modificar = get_object_or_404(Autor, id=id)
    autor_a_modificar.activo = not autor_a_modificar.activo
    autor_a_modificar.save()
    return HttpResponseRedirect(reverse('autores:listar_autores'))

class AutorUpdateView(UpdateView):
    autor = Autor
    fields = '__all__' 
    template_name = 'crear.html'
    success_url = reverse_lazy('autores:listar_autores')
    def get_queryset(self):
        return super().get_queryset().filter(id="id")

class AutorCreateView(CreateView):
    autor = Autor
    fields = ["autor","nacionalidad","fecha_nacimiento","fecha_fallecimiento","activo"] #Campos a llenar
    template_name = 'crear.html'
    success_url = reverse_lazy('autores:listar_autores')