from .models import cuusinhvien
from .serializer import cuusinhvienSerializer
from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class cuusinhvienListCreateViewSet(generics.ListCreateAPIView):
    queryset = cuusinhvien.objects.all()
    serializer_class = cuusinhvienSerializer

class cuusinhvienDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = cuusinhvien.objects.all()
    serializer_class = cuusinhvienSerializer
