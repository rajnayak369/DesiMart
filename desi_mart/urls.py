from django.urls import path,include
from django.contrib import admin
from . import views
from desi_mart.views import products,general,basket

app_name = 'desi_mart'
#adding the urls and the views method associated with the url path.
urlpatterns = [
    path('', views.general.home, name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products', views.products.all_products, name='products'),
    path('products/<str:category>', views.products.category_products, name='category_products'),
    path('products/search/', views.products.search_products, name='search_products'),
    path('product/<int:id>', views.products.product_detail, name='product_detail'),
    path('basket_add/<int:product_id>/', views.basket.basket_add, name='basket_add'),
    path('basket_remove/<int:product_id>/', views.basket.basket_remove, name='basket_remove'),
    path('basket_detail/', views.basket.basket_detail, name='basket_detail'),
    path('signup/', views.general.signup, name='signup'),
    path('place_order/', views.general.place_order, name='place_order'),
    path('order/success', views.general.order_success, name='orderplaced'),
    path('orders/', views.general.order_list, name='orders'),
    path('myorders/<int:id>', views.general.myorders, name='myorders'),
    path('order/<int:id>/', views.general.order_detail, name='order_detail'),
    path('dashboard/', views.general.dashboard, name='dashboard'),

]
