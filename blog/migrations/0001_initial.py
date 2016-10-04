# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-08-20 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', tinymce.models.HTMLField()),
                ('image', models.FileField(max_length=250, upload_to=b'')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2016, 8, 20, 13, 0, 32, 768098, tzinfo=utc))),
                ('meta_title', models.CharField(blank=True, max_length=250)),
                ('meta_description', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]