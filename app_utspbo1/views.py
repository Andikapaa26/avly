from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from app_utspbo1.forms import formJurnal
from django.shortcuts import redirect

def index(request):
    Konservasis = Konservasi.objects.all()
    data = {
        'Title' : "Daerah Konservasi Penyu di Indonesia",
        'Heading' : "Daerah Konservasi Penyu di Indonesia",
        'Konservasis' : Konservasis
    }
    return render(request, 'index.html', data)

def detail(request, id):
    detailBook = Konservasi.objects.get(pk=id)
    data = {
        'Title' : "Detail Ikan",
        'Konservasi' : detailBook,
    }
    return render(request, 'detail.html', data)


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

def deletekonservasi(request, id_konservasi):
    Jurnals = Konservasi.objects.get(id = id_konservasi)
    Jurnals.delete()

    return redirect('/index/')

# Create your views here.
