# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_contact_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.CharField(default=234, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='postcode',
            field=models.CharField(default=345, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='tele',
            field=models.CharField(default=456, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
