
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .views import ProductListView, ProductDetailSlugView


urlpatterns = [
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='list'),
    #path('admin/', ProductListView.as_view(), name='product_admin'),
]
