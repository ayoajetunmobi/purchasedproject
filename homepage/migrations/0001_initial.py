# Generated by Django 3.1 on 2021-09-15 05:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50)),
                ('contact', models.CharField(max_length=255, unique=True)),
                ('about', models.CharField(max_length=150)),
                ('quote', models.CharField(max_length=60)),
                ('university', models.CharField(default='LASU', max_length=100)),
                ('campus', models.CharField(choices=[('ojo', 'OJO'), ('epe', 'EPE'), ('lasuth', 'LASUTH')], max_length=100)),
                ('matricNo', models.CharField(blank=True, max_length=100, null=True)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='profilepic')),
                ('securityQusetion', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('matricverified', models.BooleanField(default=False)),
                ('topuser', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=4000)),
                ('searchTag', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profilepic')),
                ('date_time', models.DateField(default=datetime.datetime(2021, 9, 15, 5, 12, 47, 384488, tzinfo=utc))),
                ('username', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=100)),
                ('online', models.BooleanField(default=False)),
                ('matricverified', models.BooleanField(default=False)),
                ('topuser', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Searchdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=1000, null=True)),
                ('timesSearched', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=80)),
                ('as_buyer', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_img', models.ImageField(upload_to='media')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_product')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('read', models.BooleanField(default=False)),
                ('contacted', models.BooleanField(default=False)),
                ('user_to_review', models.CharField(blank=True, max_length=100, null=True)),
                ('my_messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_care',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportbug', models.CharField(blank=True, max_length=600, null=True)),
                ('suggestionbox', models.CharField(blank=True, max_length=600, null=True)),
                ('deactivate_account', models.CharField(blank=True, max_length=700, null=True)),
                ('reportuser', models.CharField(blank=True, max_length=700, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Contacted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
    ]
