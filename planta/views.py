from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
#mesnaje tipop cokies temporales
from django.contrib import messages
from django.urls import reverse
#gestion de errores de base de datos
from django.db import IntegrityError
from .models import Trabajador, Categoria, Producto, Produccion

# Create your views here.

def index (request):
    return render(request,"planta/index.html")


def listarTrabajador(request):
    q = Trabajador.objects.all()
    contexto = {"datos":q}
    return render(request, 'planta/trabajador/listar_trabajador.html', contexto)

def formularioTrabajador(request):
    return render(request, 'planta/trabajador/nuevo_trabajador.html')

def guardarTrabajador(request):
    try:
        if request.method == "POST":
            q = Trabajador(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                correo = request.POST["correo"]
            )
            q.save()
            messages.success(request, "trabajador guardado correctamente")
        else:
            messages.warning(request, "usted no ha enviado datos")    
            #si todo okay
    except Exception as e:
        messages.error(request, f"error:{e}")

    return redirect('planta:listarTrabajador')   

       

            

   