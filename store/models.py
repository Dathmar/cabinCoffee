from django.db import models


# Create your models here.
class Location(models.Model):
    description = models.CharField(max_length=4000)

    def __str__(self):
        return f'Location id {self.id}'


class News(models.Model):
    description = models.CharField(max_length=4000)

    def __str__(self):
        return f'News id {self.id}'

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-id']


def photo_upload(instance, filename):
    return f'photo_upload/{filename}'


class Photos(models.Model):
    image = models.ImageField(upload_to=photo_upload, height_field='image_height', width_field='image_width', null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name_plural = 'Photos'


class Brews(models.Model):
    description = models.CharField(max_length=4000)

    def __str__(self):
        return f'Brew id {self.id}'

    class Meta:
        verbose_name_plural = 'Brews'

