# Generated by Django 4.2.1 on 2023-07-18 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxyInheritApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memodel',
            options={'ordering': ['id']},
        ),
    ]
