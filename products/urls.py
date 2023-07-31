from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_list_of_products, name='index'),
    path('product/<int:id>', views.get_product, name='product'),
]