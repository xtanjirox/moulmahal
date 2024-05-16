from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=30)
    product_description = models.CharField(max_length=300, null=True, blank=True)
    product_cost_price = models.FloatField(default=0)
    product_sale_price = models.FloatField(default=0)
    product_qrcode = models.CharField(max_length=128)
    product_image = models.ImageField(null=True, blank=True)
