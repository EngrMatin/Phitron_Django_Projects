# Generated by Django 4.2.1 on 2023-07-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractClassApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
