# Generated by Django 4.1 on 2022-08-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_poll_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question_one',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question_three',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question_two',
            field=models.CharField(max_length=30),
        ),
    ]
