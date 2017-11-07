# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscricaoEvento', '0002_auto_20171016_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='tickets',
        ),
        migrations.AddField(
            model_name='inscricao',
            name='tickets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='inscricaoEvento.Ticket'),
        ),
    ]