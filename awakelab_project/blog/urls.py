
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name = 'about-blog'),
    path('reclamo/',views.reclamo),
    path('recibido/', views.recibido),
    path('contacto/', views.contacto),
    path('reclamo_detail/', views.reclamo_detail)
]
