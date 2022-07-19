from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import *
import json


def create_record(request):
  if request.method == "POST":


    body = request.POST
    img = request.FILES['picture']

    new_record = Record.objects.create(
      title      = body['title'],
      picture    = img,
      used_money = body['used_money'],
      comment    = body['comment']
    )

    new_record_json = {
      "id"         : new_record.id,
      "title"      : new_record.title,
      "picture"    : '/media/' + str(new_record.picture),
      "date"       : new_record.date,
      "comment"    : new_record.comment,
      "used_money" : new_record.used_money,
    }

    return JsonResponse({
      'status'  : 200,
      'success' : True,
      'message' : 'record생성 성공!',
      'data'    : new_record_json
    })

  return JsonResponse({
    'status'  : 405,
    'success' : False,
    'message' : 'method error',
    'data'    : None
  })

def get_record(request, id):
  if request.method == "GET":
    record = get_object_or_404(Record, pk = id)

    record_json={
      "id"         : record.id,
      "title"      : record.title,
      "date"       : record.date,
      "comment"    : record.comment,
      "used_money" : record.used_money,
      # "picture"    : record.picture,
    }

    return JsonResponse({
      'status' :200,
      'success': True,
      'message': 'record 수신 성공!',
      'data'   : record_json
    })

  return JsonResponse({
    'status' :405,
    'success': False,
    'message': 'method error',
    'data'   : None
  })


def create_detail(request, record_id):
  if request.method == "POST":

    body = request.POST
    # print(body)
    new_detail     = Detail.objects.create(
      record       = get_object_or_404(Record, pk = record_id),
      location     = body['location'],
      friends_name = body['friends_name'],
      review       = body['review']
    )

    new_detail_json={
      "id"           : new_detail.id,
      "location"     : new_detail.location,
      "friends_name" : new_detail.friends_name,
      "review"       : new_detail.review,
    }

    return JsonResponse({
      'status' : 200,
      'success': True,
      'message': 'record 생성 성공!',
      'data'   : new_detail_json
    })


  return JsonResponse({
    'status' : 405,
    'success': False,
    'message': 'method error',
    'data'   : None
  })