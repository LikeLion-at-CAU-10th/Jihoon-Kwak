from django.db import models

class  Introduce(models.Model):
  # id      = 자동생성 -->장고에서 식별을 위해 자동으로 설정하는 값
  name      = models.CharField(max_length=50, default="지훈", null=True, blank=True)
  major     = models.CharField(max_length=50, default="물리", null=True, blank=True)
  club      = models.CharField(max_length=20, default="리버풀", null=True, blank=True)
  lol_rank  = models.CharField(max_length=20, default="실버", null=True, blank=True)