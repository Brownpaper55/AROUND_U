# Generated by Django 5.0.1 on 2024-08-09 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suncity', '0013_alter_program_date_alter_program_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
