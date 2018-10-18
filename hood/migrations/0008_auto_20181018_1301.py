# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 10:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='located_at',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='hood.NeighborHood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='hood.NeighborHood'),
        ),
    ]
