from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


class Clients(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=30)
    client_address = models.CharField(max_length=100, default='Rue')
    client_phone = models.CharField(max_length=100, default='00000000')

    class Meta:
        db_table = 'clients'
        verbose_name_plural = 'clients'
        constraints = [
            models.UniqueConstraint(fields=['client_phone'], name='unique client phone')
        ]

    def __str__(self):
        return str(self.client_id) + '-' + str(self.client_name)

    def get_absolute_url(self):
        return reverse_lazy('clients-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy('clients-delete', kwargs={"pk": self.pk})


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

    def __str__(self):
        return str(self.product_id) + '-' + str(self.product_title)

    def get_absolute_url(self):
        return reverse_lazy('products-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy('products-delete', kwargs={"pk": self.pk})


class Costs(models.Model):
    cost_id = models.BigAutoField(primary_key=True)
    cost_type = models.CharField(max_length=30)
    spending_date = models.DateTimeField(default=timezone.now)
    cost_cmt = models.CharField(max_length=500, null=True, blank=True)
    cost_recipe = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'costs'
        verbose_name_plural = 'costs'

    def __str__(self):
        return str(self.cost_id) + '-' + str(self.cost_type)

    def get_absolute_url(self):
        return reverse_lazy('costs-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy('costs-delete', kwargs={"pk": self.pk})


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    total_order = models.FloatField(default=0)

    class Meta:
        db_table = 'orders'
        verbose_name_plural = 'orders'

    def get_absolute_url(self):
        return reverse_lazy('orders-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy('orders-delete', kwargs={"pk": self.pk})


class OrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, default=1, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'order_items'
        verbose_name_plural = 'order_items'


