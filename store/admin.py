from django.contrib import admin
from .models import Photos, News, Location, Brews
from .forms import NewsForm, LocationForm, BrewForm


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm


class BrewAdmin(admin.ModelAdmin):
    form = BrewForm


admin.site.register(News, NewsAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Photos)
admin.site.register(Brews, BrewAdmin)

