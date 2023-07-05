from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_ordered = models.BooleanField(default=False)

    def cal_total(self):
        self.total_price = self.item.price * self.quantity

    def __str__(self):
        return f'{self.user.username} - {self.quantity} {self.item.name}'

class Order(models.Model):
    STATUSES = (
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed')
    )
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUSES, max_length=10, default='pending')

    def __str__(self):
        return f'order no.: {self.id} | cart no.:{self.cart.id}'