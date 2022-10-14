from django.shortcuts import render
from .models import Location, News, Photos, Brews


# Create your views here.
def index(request):
    location = Location.objects.get(id=1)
    news = News.objects.filter()[:1]
    return render(request, 'store/index.html', {'location': location, 'news': news})


def about(request):
    return render(request, 'store/about.html')


def photos(request):
    photos = Photos.objects.all()
    return render(request, 'store/photos.html', {'photos': photos})


def news(request):
    news = News.objects.all()
    return render(request, 'store/news.html', {'news': news})


def brews(request):
    brews = Brews.objects.all()
    return render(request, 'store/brews.html', {'brews': brews})
