# Generated by Django 5.0.1 on 2024-06-27 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Suncity', '0005_program_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='user',
        ),
    ]