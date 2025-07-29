from django.shortcuts import render,HttpResponse
from Carro.carro import Carro

def home(request):
    carro=Carro(request)
    return render(request,"ProyectoConstrucciones/home.html")


