# Generated by Django 2.1.5 on 2020-02-02 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20200131_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postss',
            name='Pictures_file',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='postss',
            name='PostDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 2, 15, 44, 42, 157143)),
        ),
    ]