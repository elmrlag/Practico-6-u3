class Auto:
    __modelo=str
    __cPuertas=int
    __color=str
    __precio=float
    __marca=str
    def __init__(self,v1,v2,v3,v4,v5):
        self.__modelo=v1
        self.__cPuertas=v2
        self.__color=v3
        self.__precio=v4
        self.__marca=v5
    def cambiarPrecio(self):
        x=input("Ingrese el nuevo precio base: ")
        self.__precio=x
        return (self.__precio)
    def getPrecio(self):
        return(self.__precio)
    def getModelo(self):
        return(self.__modelo)
    def getcPuertas(self):
        return(self.__cPuertas)
    def getColor(self):
        return(self.__color)
    def getMarca(self):
        return(self.__marca)