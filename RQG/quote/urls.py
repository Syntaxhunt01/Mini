from django.urls import path
from .views import *

urlpatterns = [
    path('', random_quote, name='random_quote'),
    path('quote/', api_random_quote, name='api_random_quote'),
    path('add/', add_quote, name='add_quote')
]