from django.db import models
from django.utils import timezone


class Clients(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=30)
    client_address = models.CharField(max_length=100, default='Rue')
    client_phone = models.CharField(max_length=100, default='00000000')

    class Meta:
        db_table = 'clients'
        verbose_name_plural = 'clients'


class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_title = models.CharField(max_length=30)
    product_description = models.CharField(max_length=300, null=True, blank=True)
    product_cost_price = models.FloatField(default=0)
    product_sale_price = models.FloatField(default=0)
    product_quantity = models.IntegerField(default=0)
    product_qrcode = models.CharField(max_length=128)
    product_image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'products'


class Costs(models.Model):
    cost_id = models.BigAutoField(primary_key=True)
    cost_type = models.CharField(max_length=30)
    spending_date = models.DateTimeField(default=timezone.now)
    cost_cmt = models.CharField(max_length=500, null=True, blank=True)
    cost_recipe = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'costs'
        verbose_name_plural = 'costs'


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    total_order = models.FloatField(default=0)

    class Meta:
        db_table = 'orders'
        verbose_name_plural = 'orders'


class OrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'order_items'
        verbose_name_plural = 'order_items'
