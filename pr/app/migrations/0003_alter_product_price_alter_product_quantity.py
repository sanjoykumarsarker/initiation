# Generated by Django 5.0.4 on 2024-04-23 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(default='', max_length=10),
        ),
    ]
