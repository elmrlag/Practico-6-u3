from ClaseAuto import Auto
import json
class usado(Auto):
    __patente=str
    __año=int
    __km=float
    def __init__(self,v1,v2,v3,v4,v5,v6,v7,v8):
        Auto.__init__(self,v1,v2,v3,v4,v5)
        self.__patente=v6
        self.__año=v7
        self.__km=v8

    def getPatente(self):
        return(self.__patente)
    def getTipo(self):
        print("El Auto es usado")

    def cambiarPrecio(self,v1):
        if (self.__patente==v1):
            x=float(super().cambiarPrecio())
            y=int(input("Ingrese el año actual: "))
            aDif=float(self.__año-y)
            if (self.__km>100000):
                kmdisc=0.2
            else:
                kmdisc=0
            total=x-(x*(aDif/10))-(x*(kmdisc))
            print(f"El nuevo precio de venta es de {total}")

    def getPrecio(self,v1):
        return(super().getPrecio())
    def getPrecio2(self):
        return(super().getPrecio())
    
    def mostrarAuto(self):
        y=int(input("Ingrese el año actual: "))
        aDif=float(self.__año-y)
        if (self.__km>100000):
            kmdisc=0.2
        else:
            kmdisc=0
        x=super().getPrecio()
        total=x-(x*(aDif/10))-(x*(kmdisc))
        print(f"Modelo: {super().getModelo()} Cantidad de puertas: {super().getcPuertas()} Color: {super().getColor()} Precio Base: {x} Precio de Venta: {total} Marca: {super().getMarca()} Patente: {self.__patente} Año: {self.__año} Kilometraje: {self.__km}")
    
    def mostrar(self,año,y):
        v1=super().getModelo()
        v2=super().getcPuertas()
        aDif=float(self.__año-año)
        if (self.__km>100000):
            kmdisc=0.2
        else:
            kmdisc=0
        x=super().getPrecio()
        v3=x-(x*(aDif/10))-(x*(kmdisc))
        print(f"{y} \t {v1} \t\t {v2} \t\t\t {v3}")

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = super().getModelo(),
                            cPuertas = super().getcPuertas(),
                            Color = super().getColor(),
                            Precio = super().getPrecio(),
                            Marca = super().getMarca(),
                            Patente = self.__patente,
                            Ano = self.__año,
                            Km = self.__km,
                            )
            )
        return (d)

        
    