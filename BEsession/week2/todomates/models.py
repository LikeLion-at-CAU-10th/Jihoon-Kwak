from pyexpat import model
from django.db import models

class Category(models.Model):
  # id      = 자동생성 -->장고에서 식별을 위해 자동으로 설정하는 값
  title     = models.CharField(max_length=50, default="메롱", null=True, blank=True)
  view_auth = models.IntegerField(default=0, null=True, blank=True)
  color     = models.CharField(max_length=20, default="#097086", null=True, blank=True)
  pup_date  = models.DateTimeField(auto_now_add=True)