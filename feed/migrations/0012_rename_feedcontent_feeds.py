# Generated by Django 4.1.1 on 2022-10-06 02:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0011_alter_feedcontent_topic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedContent',
            new_name='Feeds',
        ),
    ]