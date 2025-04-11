# Generated by Django 5.2 on 2025-04-11 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0002_alter_autor_options_alter_autor_nacionalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.TextField()),
                ('comentario', models.CharField(max_length=100)),
                ('fecha_frase', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.autor')),
            ],
        ),
    ]
