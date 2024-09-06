from django.urls import path
from . import views

urlpatterns = [
    path('domain-checker/', views.domain_checker, name='domain_checker'),
    path('hash-checker/', views.hash_checker, name='hash_checker'),
    path('ip-checker/', views.ip_checker, name='ip_checker'),
]
