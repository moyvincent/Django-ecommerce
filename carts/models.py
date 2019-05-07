from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)
