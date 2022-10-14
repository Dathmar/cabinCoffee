from django.db import models
from django.shortcuts import reverse


def product_image_upload(instance, filename):
    return f'product_images/{filename}'


class GrindSize(models.Model):
    grind = models.CharField(max_length=25)


# Create your models here.
class Products(models.Model):
    slug = models.SlugField(max_length=4000, unique=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=4000)
    short_description = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=20)
    quantity_in_stock = models.IntegerField()
    image = models.ImageField(upload_to=product_image_upload, height_field='image_height', width_field='image_width', null=True)

    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)

    price = models.DecimalField(max_digits=7, decimal_places=2)

    grind = models.ForeignKey(GrindSize, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('products:product-page', kwargs={'product_slug': self.slug})

    def __str__(self):
        return f'{self.size} - {self.description}'

    class Meta:
        verbose_name_plural = 'Products'
