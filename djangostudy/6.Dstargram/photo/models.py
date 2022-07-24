from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
  author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photo')
  photo   = models.ImageField(upload_to='photos/%Y/%M/%d', default='photos/no_image.png')
  text    = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-updated']

  def __str__(self):
    return self.author.username + "" + self.created.strftime("%Y-%M-%d %H:%M:%S")

  def get_absolute_url(self):
    return reverse('photo:photo_detail', args=[str(self.id)])

# 상속받은 User모델은 장고에서 기본적으로 제공하는 User모델이다.
# related_name은 그 모델에 속한 하위객체를 호출할 때 사용한다.
