import cohere
from .models import Urun

# API anahtarını gir
co = cohere.Client("sI7EjDVXtpei3r6SU40vQ2zSXCyZhN0LODVpzepw")


def stok_raporu_olustur():
    """
    Veritabanından sade stok bilgilerini topla.
    """
    urunler = Urun.objects.all()
    rapor = ""
    for urun in urunler:
        rapor += f"{urun.isim}: {urun.stok} adet\n"
    return rapor


def stok_analizi_yap(rapor_metni):
    """
    Cohere Chat API ile stok analizi oluştur.
    """
    try:
        # Sohbet mesajını hazırla
        response = co.chat(
            model="command-r-plus",
            message=(
                "Aşağıdaki ürün stok raporunu analiz et. "
                "Kritik stokta (30 adetten az) olan ürünleri belirt ve genel bir değerlendirme yap:\n\n"
                f"{rapor_metni}"
            ),
            temperature=0.5,
        )

        return response.text.strip()

    except Exception as e:
        return f"Hata oluştu: {e}"