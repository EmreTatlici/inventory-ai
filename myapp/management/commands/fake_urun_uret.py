from django.core.management.base import BaseCommand
from faker import Faker
import random
from myapp.models import Urun

class Command(BaseCommand):
    help = 'Sahte ürün verisi oluşturur'

    def handle(self, *args, **kwargs):
        fake = Faker('tr_TR')

        for _ in range(50):  # 50 adet sahte ürün
            isim = fake.word().capitalize()
            fiyat = round(random.uniform(5, 500), 2)
            stok = random.randint(0, 200)

            Urun.objects.create(
                isim=isim,
                fiyat=fiyat,
                stok=stok
            )

        self.stdout.write(self.style.SUCCESS("✔ 50 sahte ürün başarıyla eklendi!"))