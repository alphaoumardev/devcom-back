# Generated by Django 4.1.1 on 2022-10-13 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0027_remove_feed_saves_feed_saves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='liked',
        ),
    ]
