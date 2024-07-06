# Generated by Django 5.0.1 on 2024-06-27 09:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suncity', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]