# Generated by Django 5.0.9 on 2024-10-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_floor_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetails',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='roomdetails',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]