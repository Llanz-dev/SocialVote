# Generated by Django 4.1 on 2022-08-29 06:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_poll_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='poll_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]