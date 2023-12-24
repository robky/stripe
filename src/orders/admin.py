from django.contrib import admin

from orders import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
