# Generated by Django 3.1 on 2021-07-24 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20210724_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_product',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2021, 7, 24, 17, 21, 35, 756375, tzinfo=utc)),
        ),
    ]
