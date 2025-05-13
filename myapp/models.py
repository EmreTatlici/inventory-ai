from django.db import models

# Create your models here.

class Urun(models.Model):
    isim = models.CharField(max_length=100)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim
