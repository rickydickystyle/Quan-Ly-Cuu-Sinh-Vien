# alumni/models.py
from django.db import models

class cuusinhvien(models.Model):
    name = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    student_id = models.CharField(max_length=10)
    # Add other fields as needed

