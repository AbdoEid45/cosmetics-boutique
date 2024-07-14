from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brands/', views.brand_list, name='brand_list'),
    path('products/', views.product_list, name='product_list'),
    path('brand/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]