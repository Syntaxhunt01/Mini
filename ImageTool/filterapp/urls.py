from django.urls import path
from .views import *
urlpatterns = [
    path('', filter_image_view, name='filter_image')
]