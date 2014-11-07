# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('evento', models.IntegerField(primary_key=True, serialize=False)),
                ('escuela', models.IntegerField(verbose_name='Clave de la escuela')),
                ('nombre_evento', models.CharField(max_length=244)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
