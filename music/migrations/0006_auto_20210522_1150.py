# Generated by Django 3.1.7 on 2021-05-22 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20210521_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_listen',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 11, 50, 43, 934597)),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_link',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]