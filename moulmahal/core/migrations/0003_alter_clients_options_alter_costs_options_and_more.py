# Generated by Django 5.0.6 on 2024-05-19 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clients_costs_products_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'clients'},
        ),
        migrations.AlterModelOptions(
            name='costs',
            options={'verbose_name_plural': 'costs'},
        ),
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name_plural': 'order_items'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'products'},
        ),
    ]