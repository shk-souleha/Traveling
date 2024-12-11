from django.shortcuts import render
from .models import Package,Place,Category
from django.views.generic import ListView,DetailView



# Create your views here.

class PackageListView(ListView):
    model = Package

class PlaceDetailView(DetailView):
    model = Package
    template_name="packages/place_detail.html"
    

def search(request):
    keyword=request.GET.get("keyword")
    packages=Package.objects.all().filter(package_destination__icontains=keyword)
    return render(request, "packages/search.html",{"packages":packages})

class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category_detail.html"
    slug_field="category_slug"
    context_object_name="category_obj"

