# Generated by Django 4.2.2 on 2023-07-05 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogconn', '0006_alter_comment_date_added_alter_uploads_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 6, 0, 5, 53, 416592)),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 6, 0, 5, 53, 416592)),
        ),
    ]
