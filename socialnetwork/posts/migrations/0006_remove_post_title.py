# Generated by Django 5.0.2 on 2024-02-17 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
