# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-27 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FILE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_url', models.CharField(max_length=255, verbose_name='URL')),
                ('file_name', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('file_url', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'file',
            },
        ),
        migrations.CreateModel(
            name='GOV_MSG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('msg_from', models.CharField(max_length=255, verbose_name='\u6765\u6e90')),
                ('msg_date', models.CharField(max_length=255, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('whole_content', models.TextField(blank=True, null=True, verbose_name='\u5168\u6587')),
                ('main_content', models.TextField(blank=True, null=True, verbose_name='\u6b63\u6587')),
                ('end_content', models.TextField(blank=True, null=True, verbose_name='\u843d\u6b3e')),
            ],
            options={
                'verbose_name': 'gov',
                'verbose_name_plural': 'gov',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]