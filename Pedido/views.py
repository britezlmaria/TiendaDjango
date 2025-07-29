from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from Carro.carro import Carro
from Pedido.models import Pedido, LineaPedido
from Tienda.models import Producto


@login_required(login_url="/autenticacion/loguear")
def hacer_pedido(request):
    if request.method != "POST":
        messages.error(request, "Método no permitido.")
        return redirect('Tienda')

    carro = Carro(request)
    if not carro.carro:
        messages.error(request, "El carrito está vacío.")
        return redirect('Tienda')

    pedido = Pedido.objects.create(user=request.user)
    lineas_pedido = []

    for key, item in carro.carro.items():
        try:
            producto = Producto.objects.get(pk=key)
        except Producto.DoesNotExist:
            messages.warning(request, f"Producto con id {key} no existe y fue omitido.")
            continue

        lineas_pedido.append(
            LineaPedido(
                producto=producto,
                cantidad=item["cantidad"],
                user=request.user,
                pedido=pedido
            )
        )

    LineaPedido.objects.bulk_create(lineas_pedido)

    try:
        send_mail(
                subject='Contacto desde el sitio',
                message='Pedido creado correctamente.',
                from_email='no-reply@miapp.com',
                recipient_list=['test@cliente.com'],
                fail_silently=False,
            )
        carro.limpiar()
        messages.success(request, "Pedido creado correctamente y correo enviado.")
        return redirect('Tienda')

    except Exception as e:
        messages.error(request, f"No se pudo enviar el correo: {str(e)}")
        carro.limpiar()
        messages.success(request, "Pedido creado correctamente, pero no se envió el correo.")
        return redirect('Tienda')
    return redirect('Tienda')

    


