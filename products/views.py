from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
  products = Product.objects.all().order_by('name')
  name_search = request.GET.get('name_search')
  if name_search:
    products = products.filter(name__icontains=name_search)
  context = {'products': products}
  return render(request, 'products/index.html', context)

def show(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  context  = {'product':product}
  return render(request, 'products/show.html', context)
              
  return