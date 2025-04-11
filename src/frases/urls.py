from django.urls import path
from . import views
from .views import (
    FrasesListView,
    VisibleListView,
    InvisibleListView,
    FrasesCreateView,
    FrasesUpdateView,
    FrasesDeleteView,
)

app_name = 'frases'

urlpatterns = [
    path('listar_frases/', FrasesListView.as_view(), name = 'listar_frases'),
    path('listar_visibles/', VisibleListView.as_view(), name = 'frases_visibles'),
    path('listar_invisibles/', InvisibleListView.as_view(), name = 'frases_invisibles'),
    path('crear_frase/', FrasesCreateView.as_view(), name = 'crear_frase'),
    path('actualizar_frase/<int:pk>/', FrasesUpdateView.as_view(), name = 'actualizar_frase'),
    path('borrar_frase/<int:pk>/', FrasesDeleteView.as_view(), name = 'borrar_frase'),
    path('listar_frases_json/', views.listar_frases_json, name = 'listar_frases_json'),
]
