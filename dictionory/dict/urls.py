from django.urls import path
from .views import *


urlpatterns = [
    path('', dictionary_view, name='dictionary')
]