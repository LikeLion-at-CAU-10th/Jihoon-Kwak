from django.urls import path
from profiles.views import create_introduce, get_introduce
from .models import *


urlpatterns = [
  path('create-introduce/', create_introduce, name = "create-introduce"),    
  path('get-introduce/<int:id>', get_introduce, name = "get-introduce"),
]
