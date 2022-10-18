from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    NIDN = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    jabatan = models.CharField(max_length=200)

# def _str_(self):
#     return self.NIP

class Fasilitas(models.Model):
    sarana = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    kualitas = models.CharField(max_length=200)
    pengelola = models.CharField(max_length=200)

# def _str_(self):
#     return self.sarana
