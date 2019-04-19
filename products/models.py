import os
import random

from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
'''
def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 34559940392)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)'''


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19, default=99.99)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/detail/{slug}/".format(slug=self.slug)

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
