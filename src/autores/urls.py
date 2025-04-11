from django.urls import path
from . import views
from .views import (
    AutorUpdateView,
    AutorCreateView,  
)
from frases.views import FrasesListView

app_name='autores'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listar/', views.listar_autores, name='listar_autores'),
    path('listar_activos/',views.autores_activos, name='autores_activos'),
    path('listar_inactivos/',views.autores_inactivos, name='autores_inactivos'),
    path('borrar/<int:id>/', views.borrar_autor, name='borrar'),
    path('detalle/<int:id>/', views.detalle_autor, name='detalle'),
    path('listar_json/', views.listar_json, name='listar_json'),
    path('estado/<int:id>', views.estado_autor, name='estado'),
    path('modificar/<int:id>/', AutorUpdateView.as_view(), name = 'modificar'),
    path('crear/<int:id>/', AutorCreateView.as_view(), name = 'crear'),
    path('autor_frases/<int:id>', FrasesListView.as_view(), name= 'autor_frases'),
]
