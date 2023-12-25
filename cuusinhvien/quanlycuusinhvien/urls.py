from django.urls import path
from .views import cuusinhvienListCreateViewSet, cuusinhvienDetailViewSet
from rest_framework import routers
from . import views

urlpatterns = [
    path('quanlycuusinhvien/', cuusinhvienListCreateViewSet.as_view(), name='cuusinhvien-list-create'),
    path('quanlycuusinhvien/<int:pk>/', cuusinhvienDetailViewSet.as_view(), name='cuusinhvien-detail'),
]
routers = routers.DefaultRouter()
routers.register('quanlycuusinhvien', views.cuusinhvienDetailViewSet)
