from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('creator-profile/<slug:poll_slug>/<uuid:poll_uuid>/', views.creator_profile, name='creator-profile'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    path('sign-out/', views.sign_out, name='sign-out'),
]
