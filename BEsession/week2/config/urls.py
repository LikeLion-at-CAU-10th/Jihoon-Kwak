from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todomates/', include('todomates.urls')),
    path('profiles/', include('profiles.urls')),
]
