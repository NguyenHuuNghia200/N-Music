# Generated by Django 3.1.7 on 2021-05-21 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210521_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='history_listen',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 16, 23, 4, 974290)),
        ),
    ]
