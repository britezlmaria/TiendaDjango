from django.conf import settings
from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import send_mail

def contacto(request):

    form=FormularioContacto()

    if request.method=="POST":
        form=FormularioContacto(data=request.POST)
        if form.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            send_mail(
                subject='Contacto desde el sitio',
                message='Gracias por contactarte con nosotros.',
                from_email='no-reply@miapp.com',
                recipient_list=['test@cliente.com'],
                fail_silently=False,
            )
            return redirect("/contacto/?valido")
    else:
        form=FormularioContacto()            
        
    return render(request,"Contacto/contacto.html",{'form':form})
