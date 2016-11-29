# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0005_auto_20161129_1425'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Manufacturer',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='brand',
            new_name='manufacturer',
        ),
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.ForeignKey(blank=True, to='Computer.Brand', null=True),
        ),
    ]
