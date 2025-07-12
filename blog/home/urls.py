from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='post'),
    path('edit/<int:pk>/', edit_post, name='edit_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
]