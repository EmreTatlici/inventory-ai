# views.py
from django.shortcuts import render
from .models import Urun
from .ai_utils import stok_analizi_yap, stok_raporu_olustur

def urun_listesi(request):
    urunler = Urun.objects.all()
    return render(request, 'urun_listesi.html', {'urunler': urunler})

def dashboard(request):
    urunler = Urun.objects.all()
    kritik_stok = [urun for urun in urunler if urun.stok < 20]  # Kritik stok filtresi
    toplam_urun = urunler.count()

    context = {
        'urunler': urunler,
        'kritik_stok': kritik_stok,
        'toplam_urun': toplam_urun,
    }
    return render(request, 'dashboard.html', context)


def ai_rapor(request):
    rapor = stok_raporu_olustur()
    analiz = stok_analizi_yap(rapor)
    return render(request, "ai_rapor.html", {"rapor": rapor, "analiz": analiz})