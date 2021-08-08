from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_url'),
    path('definite_client/<client_id>/', views.check_definite_client, name='definite_client_url'),
    path('all-users/', views.users_list, name='users_list_url'),
    path('registration/', views.registration, name='create_client_url'),
]
