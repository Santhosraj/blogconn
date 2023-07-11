# Generated by Django 4.2.2 on 2023-07-05 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogconn', '0003_uploads_no_of_likes_alter_comment_date_added_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='blogs',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 5, 23, 27, 42, 398326)),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 5, 23, 27, 42, 398326)),
        ),
    ]
