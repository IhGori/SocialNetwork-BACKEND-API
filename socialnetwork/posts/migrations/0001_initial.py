# Generated by Django 5.0.2 on 2024-02-15 03:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('body', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
