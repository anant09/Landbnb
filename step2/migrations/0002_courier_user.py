# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 23:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('step2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
