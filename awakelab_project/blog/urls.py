
from django.urls import path
from . import views
from .views import PublicacionDetalle, PublicacionCrear
urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name = 'about-blog'),
    path('reclamo/',views.reclamo),
    path('recibido/', views.recibido),
    path('contacto/', views.contacto),
    path('reclamo_detail/', views.reclamo_detail),
    path('_publicacion/<int:pk>', PublicacionDetalle.as_view(), name = 'publicacion-detalle'),
    path('publicacion/new', PublicacionCrear.as_view(), name = 'publicacion-crear')

]
