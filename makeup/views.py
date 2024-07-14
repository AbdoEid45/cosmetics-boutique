from django.shortcuts import render, get_object_or_404
from .models import Brand, Product

def home(request):
    brand_count = Brand.objects.count()
    product_count = Product.objects.count()
    return render(request, 'makeup/base_generic.html', {'brand_count': brand_count, 'product_count': product_count, 'business_name': 'Cosmetic Boutique'})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'makeup/brand_list.html', {'brands': brands, 'business_name': 'Cosmetic Boutique'})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'makeup/product_list.html', {'products': products, 'business_name': 'Cosmetic Boutique'})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, 'makeup/brand_detail.html', {'brand': brand, 'business_name': 'Cosmetic Boutique'})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product, 'business_name': 'Cosmetic Boutique'})