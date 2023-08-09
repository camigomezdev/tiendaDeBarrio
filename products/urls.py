from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_list_of_products, name='index'),
    path('product/<int:id>', views.get_product, name='product'),
    path('product/<int:id>/add_comment', views.add_new_comment, name='add_new_comment'),
]