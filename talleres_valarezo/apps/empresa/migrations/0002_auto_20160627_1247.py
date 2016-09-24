# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha',
            field=models.DateField(default=datetime.date(2016, 6, 27), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(default='imagen aqui', upload_to=b'empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(default='imagen aqui', upload_to=b'servicios'),
            preserve_default=False,
        ),
    ]
