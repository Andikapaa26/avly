from django.shortcuts import render
from django.http import HttpResponse

from app_utspbo1.forms import formLokasi
from .models import*
from app_utspbo1.forms import formJurnal
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Di buat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        ctx = {
            'form' : form,
        }
    return render(request, 'signup.html',ctx)

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    Konservasis = Konservasi.objects.all()
    data = {
        'Title' : "Daerah Konservasi Penyu di Indonesia",
        'Heading' : "Daerah Konservasi Penyu di Indonesia",
        'Konservasis' : Konservasis
    }
    return render(request, 'index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def detail(request, id):
    detailBook = Konservasi.objects.get(pk=id)
    data = {
        'Title' : "Detail Ikan",
        'Konservasi' : detailBook,
    }
    return render(request, 'detail.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahkonservasi(request):
    if request.POST:
        form = formJurnal(request.POST)
        if form.is_valid():
            form.save()
            form = formJurnal()
            judul = 'Tambah Data Daerah Konservasi'
            pesan = 'Data Berhasil Ditambahkan!'
            data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'pesan' : pesan
    }
        return render(request, 'tambahkonservasi.html', data)
    else:
        form = formJurnal()
        data ={
        'title' : 'Tambah Data Daerah Konservasi',
        'heading' : 'Tambah Data Daerah Konservasi',
        'form' : form,
    }
    return render(request, 'tambahkonservasi.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updatekonservasi(request, id):
    Jurnals = Konservasi.objects.get(id = id)
    template = "updatekonservasi.html"
    if request.POST:
        form = formJurnal(request.POST, instance=Jurnals)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"
            data ={
            'title' : "Halaman Update",
            'heading' : "Mengubah Data Konservasi",
            'form' :form,
            'pesan' : pesan,
            'Jurnal' : Jurnals,

    }
        return render(request, template, data)
    else:
        form = formJurnal(instance=Jurnals)
        data ={
        'title' : "Halaman Update",
        'heading' : "Mengubah Data Konservasi",
        'form' :form,
        'Jurnal' : Jurnals,
    }
    return render(request, template, data)
@login_required(login_url=settings.LOGIN_URL)
def deletekonservasi(request, id_konservasi):
    Jurnals = Konservasi.objects.get(id = id_konservasi)
    Jurnals.delete()

    return redirect('/index/')
@login_required(login_url=settings.LOGIN_URL)  
def tambahlokasi(request):
    if request.POST:
        form = formLokasi(request.POST)
        if form.is_valid():
            form.save()
            form = formLokasi()
            judul = 'Tambah Data Titik Lokasi'
            pesan = 'Data Berhasil Ditambahkan!'
            data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'pesan' : pesan
    }
        return render(request, 'tambahlokasi.html', data)
    else:
        form = formLokasi()
        data ={
        'title' : 'Tambah Data Titik Lokasi',
        'heading' : 'Tambah Data Titik Lokasi',
        'form' : form,
    }
    return render(request, 'tambahlokasi.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updatelokasi(request, id):
    Jurnals = Konservasi.objects.get(id = id)
    template = "updatelokasi.html"
    if request.POST:
        form = formJurnal(request.POST, instance=Jurnals)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"
            data ={
            'title' : "Halaman Update",
            'heading' : "Mengubah Titik Lokasi",
            'form' :form,
            'pesan' : pesan,
            'Jurnal' : Jurnals,

    }
        return render(request, template, data)
    else:
        form = formJurnal(instance=Jurnals)
        data ={
        'title' : "Halaman Update",
        'heading' : "Mengubah Titik Lokasi",
        'form' :form,
        'Jurnal' : Jurnals,
    }
    return render(request, template, data)
@login_required(login_url=settings.LOGIN_URL)
def deletelokasi(request, id_konservasi):
    Jurnals = Konservasi.objects.get(id = id_konservasi)
    Jurnals.delete()

    return redirect('/index/')

def LogoutPage(request):
    logout(request)
    return redirect('login')