# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kronFrame', '0015_auto_20170829_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offered',
            name='callSign',
        ),
        migrations.DeleteModel(
            name='CallSign',
        ),
    ]