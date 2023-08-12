# Generated by Django 4.2.1 on 2023-07-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=20)),
                ('mobile', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('student', models.ManyToManyField(to='manyToManyApp.student')),
            ],
        ),
    ]