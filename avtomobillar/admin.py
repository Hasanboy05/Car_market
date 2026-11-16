from django.contrib import admin
from .models import Avtomobil


@admin.register(Avtomobil)
class AvtomobilAdmin(admin.ModelAdmin):
    list_display = ('marka', 'model', 'yil', 'narx')