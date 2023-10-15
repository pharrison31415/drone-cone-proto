from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('hello/', views.hello_world),
    path('drone-statuses/', views.get_drone_statuses),
    path('drone-types/', views.get_drone_types),
    path('new-customer/', views.new_customer),
    path('customer-login/', views.customer_login),
]
