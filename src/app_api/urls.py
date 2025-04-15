from django.urls import path
from .views import (
    AutorListAPIView,
    AutorRetrieveAPIView,
)

app_name='app_api'

urlpatterns = [
    path("",AutorListAPIView.as_view(), name="listar_api"),
    path("<int:pk>/",AutorRetrieveAPIView.as_view(), name="retrieve_api"),
]
