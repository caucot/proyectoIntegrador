from django.urls import path
from . import views

app_name='autores'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listar/', views.listar_autores, name='listar_autores'),
    path('listar_activos/',views.autores_activos, name='autores_activos'),
    path('listar_inactivos/',views.autores_inactivos, name='autores_inactivos'),
    path('borrar/<int:id>/', views.borrar_autor, name='borrar'),
    path('detalle/<int:id>/', views.detalle_autor, name='detalle'),
    path('listar_json/', views.listar_json, name='listar_json'),
    path('estado/<int:id>', views.modificar_autor, name='estado'),
]
