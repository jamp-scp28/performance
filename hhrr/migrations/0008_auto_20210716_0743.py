# Generated by Django 3.0.6 on 2021-07-16 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hhrr', '0007_auto_20210714_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 12, 43, 4, 984570, tzinfo=utc)),
        ),
    ]