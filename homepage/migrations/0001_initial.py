# Generated by Django 3.1 on 2021-06-27 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('username', models.CharField(max_length=150, unique=True)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=4)),
                ('contact', models.CharField(max_length=15)),
                ('about', models.CharField(max_length=150)),
                ('quote', models.CharField(blank=True, max_length=60, null=True)),
                ('university', models.CharField(default='LASU', max_length=1)),
                ('campus', models.CharField(choices=[('ojo', 'OJO'), ('epe', 'EPE'), ('lasuth', 'LASUTH')], max_length=6)),
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
                ('searchTag', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profilepic')),
                ('date_time', models.DateField()),
                ('username', models.CharField(max_length=100)),
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
            name='Product_image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_img', models.ImageField(upload_to='product_img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_product')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
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
                ('as_A', models.CharField(default='buyer', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user_detail')),
            ],
        ),
    ]
