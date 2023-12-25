from rest_framework import serializers
from .models import cuusinhvien

class cuusinhvienSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuusinhvien
        fields = '__all__'