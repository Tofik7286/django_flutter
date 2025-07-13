from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('passport/extract/', views.passport_extract, name='passport-extract'),
]