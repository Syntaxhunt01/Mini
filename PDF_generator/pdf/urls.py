from django.urls import path
from .views import *

urlpatterns = [
    path('', generate_pdf_view, name='generate_pdf')
]