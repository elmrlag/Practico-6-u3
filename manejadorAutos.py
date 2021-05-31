from ClaseUsado import usado
from claseNuevo import nuevo
import json
from pathlib import Path
from Interfaz import Interfaz
from zope.interface import implementer

@implementer(Interfaz)
class manejador:
    __Autos=[]
    def __init__(self):
        self.__Autos=[]
    def agregarAuto(self,insert):
        x=input("El auto es usado? (si o no): ")
        v1=input("Ingrese el modelo: ")
        v2=int(input("Ingrese la cantidad de puertas: "))
        v3=input("Ingrese el color: ")
        v4=float(input("Ingrese el precio: "))
        v5=input("Ingrese la marca: ")
        if (x=="si"):
            v6=input("Ingrese la patente: ")
            v7=int(input("Ingrese el año del modelo: "))
            v8=int(input("Ingrese el kilometraje: "))
            newCar=usado(v1,v2,v3,v4,v5,v6,v7,v8)
            if (insert==False):
                self.__Autos.append(newCar)
            else:
                y=input("Ingrese la posicion en la que desea insertar el auto: ")
                y=int(y)
                self.__Autos.insert(int(y),newCar)
        else:
            v6=input("Ingrese la version (base o full): ")
            newCar=nuevo(v1,v2,v3,v4,v5,v6)
            if (insert==False):
                self.__Autos.append(newCar)
            else:
                y=input("Ingrese la posicion en la que desea insertar el auto: ")
                y=int(y)
                self.__Autos.insert(int(y),newCar)

    def mostrarAuto(self,v1):
        self.__Autos[v1].getTipo()

    def cambiarPrecio(self):
        y=input("Ingrese la patente: ")
        for x in range(0,len(self.__Autos)):
            self.__Autos[x].cambiarPrecio(y)

    def autoMasEconomico(self):
        y=0
        v1=self.__Autos[0].getPrecio2()
        v2=self.__Autos[1].getPrecio2()
        for x in range(0,len(self.__Autos)):
            if (v1>v2):
                y=x
                v1=self.__Autos[x].getPrecio(v1)
            v2=self.__Autos[x].getPrecio(v1)
        self.__Autos[y].mostrarAuto()
    def mostrarTodoLosAutos(self):
        y=int(input("Ingrese el año actual: "))
        print(f"Numero \t Modelo \t Cantidad de puertas \t Precio de venta")
        for x in range(0,len(self.__Autos)):
            self.__Autos[x].mostrar(y,x)

    def guardarEnJSON(self):
        for i in range (len(self.__Autos)):
            d = self.__Autos[i].toJSON()
            with Path("vehiculos.json").open("w", encoding="UTF-8") as destino:
                json.dump(d, destino, indent=4)
                destino.close()