# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0003_computer_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.CharField(max_length=20, null=True, verbose_name='\u54c1\u724c', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='cpu_info',
            field=models.CharField(max_length=30, null=True, verbose_name='CPU\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='hdd_info',
            field=models.CharField(max_length=50, null=True, verbose_name='\u786c\u76d8\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='m_board',
            field=models.CharField(max_length=30, null=True, verbose_name='\u4e3b\u677f\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='mac_address',
            field=models.CharField(max_length=50, null=True, verbose_name='MAC\u5730\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='mem_info',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5185\u5b58\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u7535\u8111\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='notes',
            field=models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='tv_id',
            field=models.CharField(max_length=12, null=True, verbose_name='TV_ID', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='tv_password',
            field=models.CharField(max_length=20, null=True, verbose_name='TV\u5bc6\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='user',
            field=models.CharField(max_length=30, null=True, verbose_name='\u4f7f\u7528\u8005', blank=True),
        ),
    ]
