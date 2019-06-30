# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-06-29 21:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190629_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pubished_date',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 29, 21, 0, 36, 198851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 29, 21, 0, 36, 197839, tzinfo=utc)),
        ),
    ]
