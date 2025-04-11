from django.db import models
from autores.models import Autor

# Create your models here.

class Frases(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    frase = models.TextField()
    comentario = models.CharField(max_length= 100)
    fecha_frase = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.autor}: "{self.frase}", {self.fecha_frase}'
