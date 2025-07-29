from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


class VRegistro(View):
    def get(self,request):
        form=UserCreationForm() 
        return render(request,"Registro/registro.html",{'form':form})

    def post(self,request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request,usuario)

            return redirect('Home')
        else:
            for e in form.error_messages:
                messages.error(request,form.error_messages[e])

            return render(request,"Registro/registro.html",{'form':form})


def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def loguear(request):

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre,password=contra)
            if usuario is not None:
                login(request,user=usuario)
                return redirect('Home')
            else:
                messages.error(request,"Usuario no valido")
        else:
            messages.error(request,"Informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"Registro/login.html",{'form':form})
