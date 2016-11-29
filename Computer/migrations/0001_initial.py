# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u7535\u8111\u540d\u79f0')),
                ('m_board', models.CharField(max_length=30, verbose_name='\u4e3b\u677f\u54c1\u724c')),
                ('cpu_info', models.CharField(max_length=30, verbose_name='CPU\u578b\u53f7')),
                ('mem_info', models.CharField(max_length=30, verbose_name='\u5185\u5b58\u578b\u53f7')),
                ('hdd_info', models.CharField(max_length=50, verbose_name='\u786c\u76d8\u578b\u53f7')),
                ('mac_address', models.CharField(max_length=50, verbose_name='MAC\u5730\u5740')),
                ('tv_id', models.CharField(max_length=12, verbose_name='TV_ID')),
                ('tv_password', models.CharField(max_length=20, verbose_name='TV\u5bc6\u7801')),
                ('user', models.CharField(max_length=30, verbose_name='\u4f7f\u7528\u8005')),
                ('buy_date', models.DateTimeField(verbose_name='\u542f\u7528\u65e5\u671f')),
                ('notes', models.CharField(max_length=200, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]
