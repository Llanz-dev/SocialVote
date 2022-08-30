from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/<slug:poll_slug>/<uuid:poll_uuid>/', views.vote, name='vote'),
    path('result/<slug:poll_slug>/<uuid:poll_uuid>/', views.result, name='result'),
    path('edit/<slug:poll_slug>/<uuid:poll_uuid>/', views.edit, name='edit'),
    path('delete/<slug:poll_slug>/<uuid:poll_uuid>/', views.delete, name='delete'),
    path('clear_selected_count/<slug:poll_slug>/<uuid:poll_uuid>/', views.clear_selected_count, name='clear_selected_count'),    
]