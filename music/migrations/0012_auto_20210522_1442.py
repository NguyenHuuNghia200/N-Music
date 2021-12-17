# Generated by Django 3.1.7 on 2021-05-22 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20210522_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_listen',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 14, 42, 51, 585481)),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_link',
            field=models.FileField(null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
