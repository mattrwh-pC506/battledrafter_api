# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_auto_20170509_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='label',
            field=models.CharField(default='Unnamed Draft - 2017-05-09 04:02:17.023848', max_length=100),
        ),
    ]
