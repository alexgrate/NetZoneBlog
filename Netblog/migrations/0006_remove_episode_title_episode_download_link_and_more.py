# Generated by Django 4.2.3 on 2024-04-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netblog', '0005_rename_season_episode_episode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='title',
        ),
        migrations.AddField(
            model_name='episode',
            name='Download_Link',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='episode',
            name='Subtitle_Download_Link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
