# Generated by Django 4.2.1 on 2023-07-16 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_rename_students_contractors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contractors',
            new_name='Student',
        ),
    ]