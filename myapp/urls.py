# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urun_listesi, name='urun_listesi'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('ai-rapor/', views.ai_rapor, name= 'ai_rapor'),
]