from django.contrib import admin
from django.template.response import TemplateResponse

from .models import cuusinhvien
from django.utils.html import mark_safe
from django.urls import path



class cuusinhvienAdminSite(admin.AdminSite):
    site_header = 'iSuccess'

    def get_urls(self):
        return [
                   path('course-stats/', self.stats_view)
               ] + super().get_urls()