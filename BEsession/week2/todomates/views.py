from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse
import json
from .models import *


def create_category(request):
  if request.method == "POST":

    body = json.loads(request.body.decode('utf-8'))

    new_category = Category.objects.create(
      title     = body['title'],
      view_auth = body['view_auth'],
      color     = body['color']
    )

    new_category_json = {
      "id" : new_category.id,
      "title" : new_category.title,
      "view_auth" : new_category.view_auth,
      "color" : new_category.color,
      "pup_date" : new_category.pup_date,
    }

    return JsonResponse({
    'status': 200,
    'success': True,
    'message': '생성 성공!',
    'data': new_category_json
    })

  return JsonResponse({
    'status': 405,
    'success': False,
    'message': 'method error',
    'data': None
  
  })

def get_category(request, id):
  if request.method == "GET":
    category = get_object_or_404(Category, pk = id)

    category_json = {
      "id" : category.id,
      "title" : category.title,
      "view_auth" : category.view_auth,
      "color" : category.color,
      # "pop_date" : category.pop_date,    
    }

    return JsonResponse({
      'status' : 200,
      'success' : True,
      'message' : 'category 수신 성공',
      'data' : category_json
    })

  return JsonResponse({
    'status' : 405,
    'success' : False,
    'message' : 'method error',
    'data' : None
  })