# Generated by Django 4.1.7 on 2023-05-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desi_mart', '0002_alter_product_discount_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]