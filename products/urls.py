from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('product/<slug:product_slug>/', views.product_page, name='product-page'),
    path('', views.product_list, name='product-list'),
]
