from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add/', add_poll, name='add_poll'),
    path('vote/<int:question_id>/', vote, name='vote'),
    path('result/<int:question_id>/', results, name='results'),
]