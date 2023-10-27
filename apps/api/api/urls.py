from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('hello/', views.hello_world),

    path('drone-statuses/', views.get_drone_statuses),
    path('drone-types/', views.get_drone_types),

    path('new-customer/', views.new_customer),
    # path('new-manager/', views.new_manager),
    path('new-owner/', views.new_owner),

    path('customer-login/', views.customer_login),
    path('manager-login/', views.manager_login),
    path('owner-login/', views.owner_login),
    
    path('private-customer-data/', views.private_customer_data),
    path('private-manager-data/', views.private_manager_data),
    path('private-owner-data/', views.private_owner_data),

    path('add-address/', views.post_address),
    path('my-addresses/', views.get_my_addresses),
]
