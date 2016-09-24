# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('informacion', models.CharField(max_length=1000)),
                ('revisado', models.BooleanField(default=False)),
                ('atendido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('nacimiento', models.CharField(max_length=255)),
                ('mision', models.CharField(max_length=255)),
                ('vision', models.CharField(max_length=255)),
                ('img_mision', models.ImageField(upload_to=b'empresa')),
                ('img_vision', models.ImageField(upload_to=b'empresa')),
                ('telef_convencional', models.CharField(max_length=10)),
                ('telef_celular', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=155)),
            ],
        ),
    ]
