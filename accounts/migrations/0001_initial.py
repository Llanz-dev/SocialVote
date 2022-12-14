# Generated by Django 4.1 on 2022-08-31 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_uuid', models.UUIDField(default=uuid.uuid4)),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('profile_slug', models.SlugField(default=None, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
