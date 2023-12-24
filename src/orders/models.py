from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(
        'Price in cents (multiplied by 100)',
        default=1,
        validators=[MinValueValidator(1)],
    )

    def get_real_price(self):
        return f'{self.price / 100:.2f}'

    def __str__(self):
        return self.name


class Order(models.Model):
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dt.strftime('%d-%m-%Y %H:%M')


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name='items'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name='orders',
    )
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
