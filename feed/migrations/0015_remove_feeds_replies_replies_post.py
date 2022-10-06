# Generated by Django 4.1.1 on 2022-10-06 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_alter_replies_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeds',
            name='replies',
        ),
        migrations.AddField(
            model_name='replies',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.feeds'),
        ),
    ]