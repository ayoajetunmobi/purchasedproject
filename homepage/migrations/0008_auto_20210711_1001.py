# Generated by Django 3.1 on 2021-07-11 09:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20210711_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_product',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 9, 1, 22, 953099, tzinfo=utc)),
        ),
    ]
