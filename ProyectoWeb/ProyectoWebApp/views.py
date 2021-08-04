from django.shortcuts import render,HttpResponse
from servicios.models import Servicio

def home (request):
    return render(request,"ProyectoWebApp/home.html")

def Servicios (request):
    servi=Servicio.objects.all()
    return render(request,"ProyectoWebApp/Servicios.html",{"servi":servi})

def Tienda (request):
    return render(request,"ProyectoWebApp/Tienda.html")

def Blog (request):
    return render(request,"ProyectoWebApp/Blog.html")

def Contacto (request):
    return render(request,"ProyectoWebApp/Contacto.html")
