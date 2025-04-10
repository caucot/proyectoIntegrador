from django.db import models

# Create your models here.

class Autor(models.Model):
    nacionalidades = {
        #('AR', 'Argentina'),
        #('ES', 'España'),
        #('MX', 'Mexico'),
        #('BRA', 'Brasil'),
        #('CHL', 'Chile'),
        #('USA', 'Estados Unidos'),
        "Argentina": "Argentina",
        "Boliviana": "Boliviana",
        "Brasileña": "Brasileña",
        "Chilena": "Chilena",
        "Colombiana": "Colombiana",
        "Costarricense": "Costarricense",
        "Cubana": "Cubana",
        "Dominicana": "Dominicana",
        "Ecuatoriana": "Ecuatoriana",
        "Salvadoreña": "Salvadoreña",
        "Guatemalteca": "Guatemalteca",
        "Hondureña": "Hondureña",
        "Mexicana": "Mexicana",
        "Nicaragüense": "Nicaragüense",
        "Panameña": "Panameña",
        "Paraguaya": "Paraguaya",
        "Peruana": "Peruana",
        "Puertorriqueña": "Puertorriqueña",
        "Uruguaya": "Uruguaya",
        "Venezolana": "Venezolana",
        "Española": "Española",
        "Estadounidense": "Estadounidense",
        "Canadiense": "Canadiense",
        "Francesa": "Francesa",
        "Alemana": "Alemana",
        "Italiana": "Italiana",
        "Portuguesa": "Portuguesa",
        "Británica": "Británica",
        "Irlandesa": "Irlandesa",
        "China": "China",
        "Japonesa": "Japonesa",
        "Coreana": "Coreana",
        "India": "India",
        "Rusa": "Rusa",
        "Australiana": "Australiana",
        "Sudafricana": "Sudafricana",
        "Egipcia": "Egipcia",
        "Nigeriana": "Nigeriana",
        "Keniata": "Keniata",
        "Marroquí": "Marroquí"
    }
    
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20,choices=nacionalidades.items())
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}, {self.nacionalidad}, {self.fecha_nacimiento}"
    
    class Meta:
        ordering = ['nombre']