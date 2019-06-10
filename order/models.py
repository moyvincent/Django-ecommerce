from django.db import models
from carts.models import Cart
# Create your models here.

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('shipped', 'Shipped'),
    ('paid', 'Paid'),
    ('refund', 'Refund'),
)

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    # billing_profile = 
    # billing_address = 
    # shipping address = 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, decimal_places=2, max_digits=100)
    order_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)

    def __str__(self):
        return self.order_id