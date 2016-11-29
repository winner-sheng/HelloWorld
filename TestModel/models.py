# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    GENDER_TYPES = (
        ('M', u'男'),
        ('F', u'女'),
        ('X', u'不告诉你'),
    )
    name = models.CharField(u'姓名', max_length=20)
    age = models.IntegerField(u'年龄', default=0)
    gender = models.CharField(u'性别', max_length=1, null=False, blank=False, choices=GENDER_TYPES, default='X')
    email = models.EmailField()
    tele = models.CharField(u'电话', max_length=20)
    address = models.CharField(u'地址', max_length=200)
    postcode = models.CharField(u'邮政编码', max_length=6)
    notes = models.CharField(u'备注', max_length=200)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
