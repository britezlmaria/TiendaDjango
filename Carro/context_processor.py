def importe_total(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for key, value in carro.items():
            precio = float(value["precio"])
            cantidad = int(value["cantidad"])
            total += precio * cantidad
    return {"importe_total": total}
