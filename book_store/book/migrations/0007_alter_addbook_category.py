# Generated by Django 4.2.1 on 2023-07-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_addbook_delete_add_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='category',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Poetry', 'Poetry'), ('Drama', 'Drama'), ('Novel', 'Novel'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Adventure', 'Adventure'), ('Religious', 'Religious'), ('Comedy', 'Comedy'), ('Computer Science', 'Computer Science'), ('Humor', 'Humor'), ('Horror', 'Horror')], max_length=30),
        ),
    ]