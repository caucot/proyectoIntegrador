# Generated by Django 5.2 on 2025-04-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(choices=[('Argentina', 'Argentina'), ('Boliviana', 'Boliviana'), ('Brasileña', 'Brasileña'), ('Chilena', 'Chilena'), ('Colombiana', 'Colombiana'), ('Costarricense', 'Costarricense'), ('Cubana', 'Cubana'), ('Dominicana', 'Dominicana'), ('Ecuatoriana', 'Ecuatoriana'), ('Salvadoreña', 'Salvadoreña'), ('Guatemalteca', 'Guatemalteca'), ('Hondureña', 'Hondureña'), ('Mexicana', 'Mexicana'), ('Nicaragüense', 'Nicaragüense'), ('Panameña', 'Panameña'), ('Paraguaya', 'Paraguaya'), ('Peruana', 'Peruana'), ('Puertorriqueña', 'Puertorriqueña'), ('Uruguaya', 'Uruguaya'), ('Venezolana', 'Venezolana'), ('Española', 'Española'), ('Estadounidense', 'Estadounidense'), ('Canadiense', 'Canadiense'), ('Francesa', 'Francesa'), ('Alemana', 'Alemana'), ('Italiana', 'Italiana'), ('Portuguesa', 'Portuguesa'), ('Británica', 'Británica'), ('Irlandesa', 'Irlandesa'), ('China', 'China'), ('Japonesa', 'Japonesa'), ('Coreana', 'Coreana'), ('India', 'India'), ('Rusa', 'Rusa'), ('Australiana', 'Australiana'), ('Sudafricana', 'Sudafricana'), ('Egipcia', 'Egipcia'), ('Nigeriana', 'Nigeriana'), ('Keniata', 'Keniata'), ('Marroquí', 'Marroquí')], max_length=20),
        ),
    ]
