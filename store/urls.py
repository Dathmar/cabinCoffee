from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('photos/', views.photos, name='photos'),
    path('news/', views.news, name='news'),
    path('brews/', views.brews, name='brews')
]
