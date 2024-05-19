from django.contrib import admin
from . import models

admin.site.register(models.Clients)
admin.site.register(models.Products)
admin.site.register(models.Orders)
admin.site.register(models.OrderItems)
admin.site.register(models.Costs)
