from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='home'),

    # Donor Section
    path('donors/', views.donors_list, name='donors_list'),
    path('donors/add/', views.add_donor, name='add_donor'),
    path('donors/<int:donor_id>/donate/', views.record_donation, name='record_donation'),

    # Blood Request Section
    path('requests/', views.requests_list, name='requests_list'),
    path('requests/add/', views.add_request, name='add_request'),
    path('requests/<int:request_id>/fulfill/', views.fulfill_request, name='fulfill_request'),

    # Authentication (Login / Register / Logout)
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
