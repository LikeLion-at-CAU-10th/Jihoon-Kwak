from django.urls import path
from .views import create_record, get_record, create_detail


urlpatterns = [
  path('create-record', create_record, name="create-record" ),
  path('get-record/<int:id>', get_record, name="get-record" ),
  path('create-detail/<int:record_id>', create_detail, name="create-detail" ),
]