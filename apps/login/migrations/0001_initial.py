# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=75, null=True)),
                ('last_name', models.CharField(blank=True, max_length=75, null=True)),
                ('username', models.CharField(blank=True, max_length=75, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('dob_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('user_level', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
