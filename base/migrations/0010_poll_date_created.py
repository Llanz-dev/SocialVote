# Generated by Django 4.1 on 2022-08-29 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_poll_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
