# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('permissions', models.ManyToManyField(to="orm['auth.Permission']", symmetrical=False, blank=True)),
            ],
            options={"db_table": 'auth_group'}
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('codename', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(to="orm['contenttypes.ContentType']"))
                ('id', models.AutoField(primary_key=True))
                ('name', models.CharField(max_length=50))
            ],
            options={
                "ordering": ['content_type__app_label', 'content_type__model', 'codename'],
                'unique_together': (('content_type', 'codename'),),
                "db_table": 'auth_group'
            }
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('date_joined', models.DateTimeField(default=datetime.datetime.now())),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('groups', models.ManyToManyField(to="orm['auth.Group']", db_table="auth_user_groups")),
                ('id', models.AutoField(primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=datetime.datetime.now())),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('password', models.CharField(max_length=128)),
                ('user_permissions', models.ManyToManyField(to="orm['auth.Permission']", symmetrical=False, blank=True, db_table='auth_user_user_permissions'))
                ('username', models.CharField(unique=True, max_length=30))
            ],
            options={
                "db_table": 'auth_user'
            }
        ),

        migrations.CreateModel(
            name='RememberToken',
            options={"db_table": "auth_remember_remembertoken"},
            fields=[
                ('created', models.DateTimeField(default=datetime.datetime.now(), blank=True)),
                ('created_initial', models.DateTimeField()),
                ('token_hash', models.CharField(max_length=128, primary_key=True)),
                ('user', models.ForeignKey(related_name="remember_me_tokens", to="orm['auth.User']"))
            ]

        ),
        migrations.CreateModel(
            name='ContentType',
            options={'db_table': 'django_content_type', 'unique_together': (('app_label', 'model'),), 'ordering': ['name']},
            fields=[
                ('app_label', models.CharField(max_length=100))
                ('id', models.AutoField(primary_key=True)),
                ('model', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100))
            ])
    ]
