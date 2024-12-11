from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.PackageListView.as_view(),name="packages"),
    path('detail/<int:pk>/',views.PlaceDetailView.as_view(),name="place-detail"),
    path('search/',views.search,name="search"),
    path('<slug:slug>/',views.CategoryDetailView.as_view(),name="category-detail"),
    path('booking/',include('booking.urls'))
    
    
]