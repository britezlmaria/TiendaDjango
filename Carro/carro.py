class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self,producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.actualizar()

    def actualizar(self):
        self.session["carro"]=self.carro
        self.session.modified=True


    def eliminar(self,producto):
        producto.id=str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.actualizar()

    def restar(self,producto):
        for key,value in self.carro.items():
                if key==str(producto.id):
                    if(value["cantidad"]>1 and float(value["precio"])-producto.precio>0):
                        value["cantidad"]=value["cantidad"]-1
                        value["precio"]=float(value["precio"])-producto.precio
                        break
                    else:
                        self.eliminar(producto)
                        break
        self.actualizar()


    def limpiar(self):
        self.session["carro"]={}
        self.session.modified=True
