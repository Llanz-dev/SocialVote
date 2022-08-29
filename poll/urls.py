"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from base import views as base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view.home, name='home'),
    path('create/', base_view.create, name='create'),
    path('vote/<slug:poll_slug>/<uuid:poll_uuid>/', base_view.vote, name='vote'),
    path('result/<slug:poll_slug>/<uuid:poll_uuid>/', base_view.result, name='result'),
    path('edit/<slug:poll_slug>/<uuid:poll_uuid>/', base_view.edit, name='edit'),
    path('delete/<slug:poll_slug>/<uuid:poll_uuid>/', base_view.delete, name='delete'),
    path('clear_selected_count/<slug:poll_slug>/<uuid:poll_uuid>/', base_view.clear_selected_count, name='clear_selected_count'),    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)