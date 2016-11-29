# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0005_remove_contact_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default=b'X', max_length=1, verbose_name='\u6027\u522b', choices=[(b'M', '\u7537'), (b'F', '\u5973'), (b'X', '\u4e0d\u544a\u8bc9\u4f60')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.IntegerField(default=0, verbose_name='\u5e74\u9f84'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u59d3\u540d'),
        ),
    ]
