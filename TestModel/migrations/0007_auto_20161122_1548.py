# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_auto_20161122_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=200, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.CharField(max_length=200, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postcode',
            field=models.CharField(max_length=6, verbose_name='\u90ae\u653f\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tele',
            field=models.CharField(max_length=20, verbose_name='\u7535\u8bdd'),
        ),
    ]
