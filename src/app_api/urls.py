from django.urls import path
from .views import (
    AutorListAPIView,
    AutorCreateAPIView,
    AutorRetrieveDestroyAPIView,
    FraseListCreateAPIView,
    FraseRetrieveDestroyAPIView,
)

app_name='app_api'

urlpatterns = [
    path("", AutorListAPIView.as_view(), name="listar_api"),
    path("crear/", AutorCreateAPIView.as_view(), name="crear_api"),
    path("<int:pk>/", AutorRetrieveDestroyAPIView.as_view(), name="retrieve_api"),
    path("frases/", FraseListCreateAPIView.as_view(), name="frases_api"),
    path("frases/<int:pk>/", FraseRetrieveDestroyAPIView.as_view(), name="frases_retrieve_api"),
]
