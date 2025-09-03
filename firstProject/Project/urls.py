from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('create/', views.product_create_view, name="Product_create"),
    path('list/', views.product_list_view, name="Product_list"),
    path('update/<int:product_id>/', views.product_update_view, name="Product_update"),
    path('delete/<int:product_id>/', views.product_delete_view, name="Product_delete"),
]