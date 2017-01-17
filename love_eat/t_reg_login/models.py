# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from tutils.tjson import TJsonTools

# Create your models here.
sex_choices = (
    ('0', '女'),
    ('1', '男'),
)


class Family(models.Model):
    """
    家庭名称
    """
    name = models.CharField(max_length=128,primary_key=True)#家庭名称
    passwd = models.CharField(max_length=128)#家庭密码
     
    def __unicode__(self):
        return TJsonTools.tJsonEncode(self)


class Person(models.Model):
    """
    个人信息
    """
    name = models.CharField(max_length=128)#姓名
    sex = models.CharField(max_length=4, choices=sex_choices)#性别
    mobile = models.CharField(max_length=32)#手机号
    age = models.IntegerField()#年龄
    addr = models.CharField(max_length=256)#地址
    entry = models.ForeignKey(Family)#所属家庭
     
    def __unicode__(self):
        return TJsonTools.tJsonEncode(self)

