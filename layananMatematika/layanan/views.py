from django.shortcuts import render
from . models import Dosen, Fasilitas
# Create your views here.
def index(request):
    return render(request, 'index.html')

def visi(request):
    return render(request, 'visi.html')

def struktur(request):
    return render(request, 'struktur.html')

def dosen(request):

    dosen = Dosen.objects.all()
    konteks = {
        'dataDosen': dosen,
    }
    return render(request, 'dosen.html', konteks)

def fasilitas(request):

    fasilitas = Fasilitas.objects.all()
    konteks = {
        'dataFasilitas': fasilitas,
    }
    return render(request, 'fasilitas.html', konteks)

def akreditasi(request):
    return render(request, 'akreditasi.html')