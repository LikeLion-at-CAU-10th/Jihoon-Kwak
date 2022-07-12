from django.contrib import admin
from django.urls import path
from todomates.views import create_category, get_category
from .models import *


urlpatterns = [
  path('create-category/', create_category, name = "create-category"),    
  path('get_category/<int:id>', get_category, name = 'get-category')
]
