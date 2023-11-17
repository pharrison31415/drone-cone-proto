from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('hello/', views.hello_world),

    path('delivery-count/', views.get_delivery_count),

    path('cone-types/', views.get_cone_types),
    path('ice-cream-types/', views.get_ice_cream_types),
    path('topping-types/', views.get_topping_types),

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
    path('delete-address/', views.delete_address),
    path('my-addresses/', views.get_my_addresses),

    path('add-drone/', views.add_drone),
    path('my-drones/', views.get_my_drones),
    path('update-drone/', views.update_drone),

    path('new-order/', views.new_order),
    path('order-delivered/', views.order_delivered),

    path('inventory/', views.get_inventory),
    path('manager-revenues/', views.get_manager_revenues),
    path('manager-costs/', views.get_manager_costs),
    path('purchase-inventory/', views.purchase_inventory),

    path('new-message/', views.new_message),
]
