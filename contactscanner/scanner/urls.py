from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_contacts, name='upload_contacts'),
    path('scan/', views.scan_number, name='scan_number'),
]
