# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0002_auto_20161122_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='brand',
            field=models.CharField(default=1, max_length=20, verbose_name='\u54c1\u724c'),
            preserve_default=False,
        ),
    ]
