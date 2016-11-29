# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    manufacturer = models.CharField(u'品牌', max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.manufacturer


class Computer(models.Model):
    name = models.CharField(u'电脑名称', max_length=30, null=True, blank=True)
#    brand = models.ForeignKey(Manufacturer, null=True, blank=True)
    brand = models.CharField(u'品牌', max_length=20, null=True, blank=True)
    m_board = models.CharField(u'主板信息', max_length=30, null=True, blank=True)
    cpu_info = models.CharField(u'CPU信息', max_length=30, null=True, blank=True)
    mem_info = models.CharField(u'内存信息', max_length=30, null=True, blank=True)
    hdd_info = models.CharField(u'硬盘信息', max_length=50, null=True, blank=True)
    mac_address = models.CharField(u'MAC地址', max_length=50, null=True, blank=True)
    tv_id = models.CharField(u'TV_ID', max_length=12, null=True, blank=True)
    tv_password = models.CharField(u'TV密码', max_length=20, null=True, blank=True)
    user = models.CharField(u'使用者', max_length=30, null=True, blank=True)
    buy_date = models.DateTimeField(u'启用日期', auto_now=True)
    notes = models.CharField(u'备注', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name


