# Generated by Django 4.1 on 2022-08-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_poll_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(max_length=65),
        ),
    ]
