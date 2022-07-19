from distutils.command.upload import upload
from turtle import title
from django.db import models


class Record(models.Model):
  title      = models.CharField(max_length=50, null=True, blank=True)
  date       = models.DateTimeField(auto_now_add=True)
  picture    = models.ImageField(upload_to = 'diary', null=True, blank=True)
  used_money = models.IntegerField(default=0, null=True, blank=True)
  comment    = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.title, self.id


class Detail(models.Model):
  record       = models.ForeignKey('Record', on_delete=models.CASCADE, null=True, blank=True)
  location     = models.CharField(max_length=50, null=True, blank=True)
  friends_name = models.CharField(max_length=50, null=True, blank=True)
  review       = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.location