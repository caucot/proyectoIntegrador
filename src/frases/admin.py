from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Frases)
class FrasesAdmin(admin.ModelAdmin):
    list_display = ['autor','frase','comentario','fecha_frase','created_at','updated_at']
    list_filter = ['visible']
    search_fields = ['autor']