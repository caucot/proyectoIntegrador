from rest_framework.serializers import ModelSerializer
from autores.models import Autor
from frases.models import Frases

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['pk','nombre','nacionalidad','fecha_nacimiento','fecha_fallecimiento','activo']


class FraseSerializer(ModelSerializer):
    class Meta:
        model = Frases
        fields = '__all__'


