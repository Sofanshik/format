from django.urls import path
from .views import *

urlpatterns = [
    path('', ClientListView.as_view(), name='main_url'),
    path('client_is_not_active/<slug:client_id>/', ClientIsNotActive.as_view(), name='client_is_not_active_url'),
    path('definite_client/<slug:client_id>/', ClientDetailView.as_view(), name='definite_client_url'),
    path('client_update/<slug:client_id>/', ClientUpdateView.as_view(), name='client_update_url'),
    path('all-users/', users_list, name='users_list_url'),
    path('registration/', ClientCreateView.as_view(), name='create_client_url'),
    path('test/', TestView.as_view(), name='test')
]
