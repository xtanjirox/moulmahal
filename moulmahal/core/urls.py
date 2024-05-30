from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r'', login_required(views.home), name='home'),

    path(r'products', views.ProductListView.as_view(), name='products-list'),
    path(r'products/create', views.ProductCreateView.as_view(), name='products-create'),
    path(r'products/update/<pk>', views.ProductUpdateView.as_view(), name='products-update'),
    path(r'products/delete/<pk>/', views.ProductDeleteView.as_view(), name='products-delete'),

    path(r'costs', views.CostListView.as_view(), name='costs-list'),
    path(r'costs/create', views.CostCreateView.as_view(), name='costs-create'),
    path(r'costs/update/<pk>', views.CostUpdateView.as_view(), name='costs-update'),
    path(r'costs/delete/<pk>/', views.CostDeleteView.as_view(), name='costs-delete'),

    path(r'clients', views.ClientListView.as_view(), name='clients-list'),
    path(r'clients/create', views.ClientCreateView.as_view(), name='clients-create'),
    path(r'clients/update/<pk>', views.ClientUpdateView.as_view(), name='clients-update'),
    path(r'clients/delete/<pk>/', views.ClientDeleteView.as_view(), name='clients-delete'),

    path(r'orders', views.OrderListView.as_view(), name='orders-list'),
    path(r'orders/create', views.OrderCreateView.as_view(), name='orders-create'),
    path(r'orders/update/<pk>', views.OrderUpdateView.as_view(), name='orders-update'),
    path(r'orders/delete/<pk>/', views.OrderDeleteView.as_view(), name='orders-delete'),

    path(r'order_items', views.OrderItemsListView.as_view(), name='order_items-list'),
    path(r'order_items/create', views.OrderItemCreateView.as_view(), name='order_items-create'),
    path(r'order_items/update/<pk>', views.OrderItemUpdateView.as_view(), name='order_items-update'),
    path(r'order_items/delete/<pk>/', views.OrderItemDeleteView.as_view(), name='order_items-delete'),

    path(r'cart/', views.cart_views, name='cart_views'),

    path(r'logout/', views.LogoutView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")), ]
