# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0004_auto_20161123_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=30, null=True, verbose_name='\u54c1\u724c', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.ForeignKey(to='Computer.Brand'),
        ),
    ]
