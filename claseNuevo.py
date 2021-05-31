from ClaseAuto import Auto
import json
class nuevo(Auto):
    __version=str
    def __init__(self,v1,v2,v3,v4,v5,v6):
        Auto.__init__(self,v1,v2,v3,v4,v5)
        self.__version=v6
    def getTipo(self):
        print("El Auto es nuevo")
    def cambiarPrecio(self,v1):
        return()
    def getPrecio(self,v1):
        return(v1+1)
    def getPrecio2(self):
        return(super().getPrecio())
    def mostrarAuto(self):
        x=super().getPrecio()
        if (self.__version=="Full"):
            verPer=0.2
        else:
            verPer=0
        print(f"Modelo: {super().getModelo()} Cantidad de puertas: {super().getcPuertas()} Color: {super().getColor()} Precio Base: {x} Precio de venta: {x+x*0.10+x*0.2} Marca: {super().getMarca()} Version: {self.__version}")
    
    def mostrar(self,año,y):
        v1=super().getModelo()
        v2=super().getcPuertas()
        x=super().getPrecio()
        if (self.__version=="Full"):
            verPer=0.2
        else:
            verPer=0
        v3=x+x*verPer+x*0.10
        print(f"{y} \t {v1} \t\t {v2} \t\t\t {v3}")

    def guardar(self):
        datos=[{
            "modelo":super().getModelo(),
            "cPuertas":super().getcPuertas(),
            "Color":super().getColor(),
            "Precio":super().getPrecio(),
            "Marca":super().getMarca(),
            "Version":self.__version
        }]
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = super().getModelo(),
                            cPuertas = super().getcPuertas(),
                            Color = super().getColor(),
                            Precio = super().getPrecio(),
                            Marca = super().getMarca(),
                            Version = self.__version
                            )
            )
        return (d)