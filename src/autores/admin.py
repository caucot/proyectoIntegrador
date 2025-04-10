from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre','nacionalidad','activo','fecha_nacimiento','fecha_fallecimiento','created_at','updated_at']
    list_filter = ['activo']
    search_fields = ['nombre']