# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-24 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200123_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='kategori',
            field=models.CharField(choices=[('Blog', 'Blog'), ('Jurnal', 'Jurnal'), ('Berita', 'Berita')], default='Blog', max_length=20),
        ),
    ]
