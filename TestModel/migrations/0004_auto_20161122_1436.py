# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_auto_20161121_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sex',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
