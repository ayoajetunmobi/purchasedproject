# Generated by Django 3.1 on 2021-06-28 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210628_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_detail',
            old_name='baseuser',
            new_name='user',
        ),
    ]
