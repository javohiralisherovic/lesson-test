# Generated by Django 3.1.4 on 2022-05-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]