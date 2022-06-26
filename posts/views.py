from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# Create your views here.


def http_response(request):
  if request.method == "GET":
    return HttpResponse("Hello World!")

def json_response(request):
  if request.method == "GET":
    data = {
      'name' : 'jihoon',
      'school' : 'cau',
      'club' : 'liverpool'
    }
    return JsonResponse(data = data)

def index(request):
  if request.method == 'POST':
    name = request.POST.get('name')

    context = {
      'name' : name
    }

    return render(request, 'index.html', context = context)

  else:
    return render(request, 'index.html')