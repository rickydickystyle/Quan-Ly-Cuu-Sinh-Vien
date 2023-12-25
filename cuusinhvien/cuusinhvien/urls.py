from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quanlycuusinhvien.urls')),
]
