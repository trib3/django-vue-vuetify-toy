"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path

from .api.views import index_view, ambassadors


urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/ambassadors/
    path('api/ambassadors/', ambassadors),
    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]
