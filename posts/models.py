from django.db import models

# Create your models here.

class Post(models.Model):
  post_id = models.AutoField(primary_key = True)
  writer = models.CharField(max_length=30)
  content = models.TextField()