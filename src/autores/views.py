from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse 

from .models import Autor

# Create your views here.

def inicio(request):
    return render(request, 'app_templates/inicio.html')


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request,
                'app_templates/listar.html',
                  {'autores': autores})
    
def autores_activos(request):
    autores = Autor.objects.all().filter(activo=True)
    return render(request,
                'app_templates/listar.html',
                  {'autores': autores})

def autores_inactivos(request):
    autores = Autor.objects.all().filter(activo=False)
    return render(request,
                'app_templates/listar.html',
                  {'autores': autores})

def listar_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    return JsonResponse(autores_json, safe=False)


def detalle_autor(request,id):
    autor  = get_object_or_404(Autor, id=id)
    return render(request,
                  'app_templates/detalle.html',
                  {'autor': autor})

def borrar_autor(request, id):
    autor_a_borrar = get_object_or_404(Autor, id=id)
    autor_a_borrar.delete() 
    return HttpResponseRedirect(reverse('autores:listar_autores'))

def modificar_autor(request,id):
    autor_a_modificar = get_object_or_404(Autor, id=id)
    autor_a_modificar.activo = not autor_a_modificar.activo
    autor_a_modificar.save()
    return HttpResponseRedirect(reverse('autores:listar_autores'))

