# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Task',
        ),
    ]
