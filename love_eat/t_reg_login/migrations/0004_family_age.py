# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_reg_login', '0003_family_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
