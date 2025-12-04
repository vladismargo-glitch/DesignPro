from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('profile/', views.profile_view, name="profile"),
    path('logout/', views.logout_view, name="logout"),
    path('create_order/', views.create_order_view, name='create_order'),
    path('my_orders/', views.my_orders_view, name='my_orders'),
    path('all_orders/', views.all_orders_view, name='all_orders'),
    path('order/<int:order_id>/change-status/', views.change_status_view, name='change_status_order'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('add_category/', views.category_management_view, name='category_management'),
]
