# Generated by Django 4.1.1 on 2022-09-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        ('feed', '0007_remove_feedcontent_topic_feedcontent_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedcontent',
            name='topic',
        ),
        migrations.AddField(
            model_name='feedcontent',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='topics.topics'),
        ),
    ]
