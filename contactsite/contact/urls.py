from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('messages/', views.view_messages, name='view_messages'),

]