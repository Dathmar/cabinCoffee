from django.shortcuts import render
from .models import Location, News

# Create your views here.
def index(request):
    location = Location.objects.get(id=1)
    news = News.objects.filter()
    return render(request, 'store/index.html', {'location': location, 'news': news})


def about(request):
    return render(request, 'store/about.html')
