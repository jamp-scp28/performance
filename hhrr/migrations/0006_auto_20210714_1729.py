# Generated by Django 3.0.6 on 2021-07-14 22:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hhrr', '0005_auto_20210714_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 22, 29, 36, 109242, tzinfo=utc)),
        ),
    ]
