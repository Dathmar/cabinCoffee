from django.db import models
from django.shortcuts import reverse


def product_image_upload(instance, filename):
    return f'product_images/{filename}'


# Create your models here.
class Products(models.Model):
    slug = models.SlugField(max_length=4000, unique=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=4000)
    size = models.CharField(max_length=20)
    quantity_in_stock = models.IntegerField()
    image = models.ImageField(upload_to=product_image_upload, height_field='image_height', width_field='image_width', null=True)

    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)

    price = models.DecimalField(max_digits=7, decimal_places=2)

    def get_absolute_url(self):
        return reverse('products:product-page', kwargs={'product_slug': self.slug})
