from django.contrib.auth.models import User
from django.db import models
from products.models import Product
from django.db.models.signals import post_save, pre_save, m2m_changed


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("card_id", None)
        qs = Cart.objects.all().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

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
    subtotal = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_reciever(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.product.all()
        total = 0
        for x in products:
            total = total + x.price 
        print(total)
        instance.subtotal = total
        instance.save()
m2m_changed.connect(m2m_changed_cart_reciever, sender=Cart.product.through)

def pre_save_cart_reciever(sender, instance, *args, **kwrags):
    instance.total = instance.subtotal

pre_save.connect(pre_save_cart_reciever, sender=Cart)