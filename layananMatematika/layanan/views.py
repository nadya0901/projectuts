from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def visi(request):
    return render(request, 'visi.html')

def struktur(request):
    return render(request, 'struktur.html')

def dosen(request):
    return render(request, 'dosen.html')

def kalender(request):
    return render(request, 'kalender.html')

def fasilitas(request):
    return render(request, 'fasilitas.html')

def akreditasi(request):
    return render(request, 'akreditasi.html')