# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-16 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='Profile_pic'),
        ),
    ]