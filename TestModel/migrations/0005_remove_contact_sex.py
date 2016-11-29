# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0004_auto_20161122_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='sex',
        ),
    ]
