# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u7535\u8111\u540d\u79f0')),
                ('m_board', models.CharField(max_length=30, verbose_name='\u4e3b\u677f\u4fe1\u606f')),
                ('cpu_info', models.CharField(max_length=30, verbose_name='CPU\u4fe1\u606f')),
                ('mem_info', models.CharField(max_length=30, verbose_name='\u5185\u5b58\u4fe1\u606f')),
                ('hdd_info', models.CharField(max_length=50, verbose_name='\u786c\u76d8\u4fe1\u606f')),
                ('mac_address', models.CharField(max_length=50, verbose_name='MAC\u5730\u5740')),
                ('tv_id', models.CharField(max_length=12, verbose_name='TV_ID')),
                ('tv_password', models.CharField(max_length=20, verbose_name='TV\u5bc6\u7801')),
                ('user', models.CharField(max_length=30, verbose_name='\u4f7f\u7528\u8005')),
                ('buy_date', models.DateTimeField(auto_now=True, verbose_name='\u542f\u7528\u65e5\u671f')),
                ('notes', models.CharField(max_length=200, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.DeleteModel(
            name='Computers',
        ),
    ]
