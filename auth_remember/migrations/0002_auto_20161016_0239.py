# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 00:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_remember', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remembertoken',
            options={'ordering': ('-created',), 'verbose_name': 'Remember Token', 'verbose_name_plural': 'Remember Tokens'},
        ),
        migrations.AlterField(
            model_name='remembertoken',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='remembertoken',
            name='created_initial',
            field=models.DateTimeField(editable=False, verbose_name='Created Initially'),
        ),
        migrations.AlterField(
            model_name='remembertoken',
            name='token_hash',
            field=models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='Token Hash'),
        ),
        migrations.AlterField(
            model_name='remembertoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remember_me_tokens', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
