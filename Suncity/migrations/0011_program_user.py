# Generated by Django 5.0.1 on 2024-06-27 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suncity', '0010_remove_program_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]