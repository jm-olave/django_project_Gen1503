from django.shortcuts import render
from .models import Publicacion
from .forms import ContactForm, ReclamoForm
def home(request):
    contexto = {
        'posts': Publicacion.objects.all()
    }
    return render(request, 'blog/home.html', contexto)

def about(request):
    return render(request,'blog/about.html')

def sumar(request, numero1, numero2):
    resultado  = numero1+numero2
    return render(request,'blog/about.html', {"numero": resultado, "valor": "esto es un valor de contexto" })

def reclamo(request):
    return render(request, 'blog/reclamo.html')

def recibido(request):
    datos  = request.GET
    email = datos["email"]
    comentario = datos["reclamo"]
    print(email, comentario)
    return render(request, 'blog/reclamo.html', {"mensaje": "Datos recibidos", "email": email, "comentario": comentario} )


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            cuerpo = form.cleaned_data["cuerpo"]
            print(nombre,email,cuerpo)
    form  = ContactForm()
    return render(request, 'blog/contacto.html', {'form': form})


def reclamo_detail(request):
    if request.method == 'POST':
        form = ReclamoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            cuerpo = form.cleaned_data["cuerpo"]
            print(nombre, cuerpo, "Funciona")
            form.save()
    form  = ReclamoForm()
    return render(request, 'blog/contacto.html', {'form': form})