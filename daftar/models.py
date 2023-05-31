from django.db import models


# Create your models here.
class Pendaftaran(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=75)
    no_telp = models.CharField(max_length=17)

    def __str__(self):
        return self.nama
