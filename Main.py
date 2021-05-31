from ClaseAuto import Auto
from manejadorAutos import manejador
import os
import sys
from Interfaz import Interfaz
if __name__=='__main__':
    autos=manejador()
    bandera=0
    while(bandera!=8):
        os.system('cls')
        print("1- Insertar un vehículo en la colección en una posición determinada.")
        print("2- Agregar un vehículo a la colección.")
        print("3- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
        print("4- Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
        print("5- Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
        print("6- Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print("7- Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
        print("8- Salir.")
        bandera=int(input("opcion: "))
        
        if (bandera==1):
            os.system('cls')
            autos.agregarAuto(True)
            os.system("pause")
        if(bandera==2):
            os.system('cls')
            autos.agregarAuto(False)
            os.system("pause")
        if(bandera==3):
            os.system('cls')
            x=int(input("Ingrese la posicion del auto: "))
            autos.mostrarAuto(x)
            os.system("pause")
        if(bandera==4):
            os.system('cls')
            autos.cambiarPrecio()
            os.system("pause")
        if(bandera==5):
            os.system('cls')
            autos.autoMasEconomico()
            os.system("pause")
        if(bandera==6):
            os.system('cls')
            autos.mostrarTodoLosAutos()
            os.system("pause")
        if(bandera==7):
            autos.guardarEnJSON()
            os.system("pause")