from django.forms import ModelForm
from django import forms
from app_utspbo1.models import *

class formJurnal(ModelForm):
    class Meta:
        model = Konservasi
        fields = '__all__'

        widgets = {
            'provinsi' : forms.TextInput({'class': 'form-control','placeholder': 'Provinsi', 'required' : 'required' }),
            'kota' : forms.TextInput({'class': 'form-control','placeholder': 'Kota', 'required' : 'required' }),
            'jenis_penyu' : forms.TextInput({'class': 'form-control','placeholder': 'Jenis Penyu', 'required' : 'required' }),
            'img' : forms.TextInput({'class': 'form-control','placeholder': 'Nama File Foto Konservasi', 'required' : 'required' }),
            'status_keberadaan' : forms.Select({'class': 'form-control','placeholder': ' Status Keberadaan', 'required' : 'required' }),
        }