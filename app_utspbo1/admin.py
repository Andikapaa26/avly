from dataclasses import field
from django.contrib import admin

# Register your models here.
from .models import *

class bukuadmin(admin.ModelAdmin):
    list_display = ['provinsi', 'kota', 'jenis_penyu', 'Status_keberadaan', 'img']
    list_per_page = 4

admin.site.register(Konservasi, bukuadmin)
admin.site.register(Status)
