# Generated by Django 4.1.2 on 2022-10-20 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0032_feed_viewes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='viewes',
            new_name='views',
        ),
    ]