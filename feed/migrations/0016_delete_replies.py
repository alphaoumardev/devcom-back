# Generated by Django 4.1.1 on 2022-10-06 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_remove_feeds_replies_replies_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Replies',
        ),
    ]