# Generated by Django 4.1.1 on 2022-10-11 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0022_rename_feeds_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='liked',
        ),
    ]
