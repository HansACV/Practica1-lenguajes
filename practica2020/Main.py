import json

Lista=[]


class Dato:
    Nombre=''
    Edad=0
    Activo=True
    Promedio=0.0

    def __init__(self,Nombre,Edad,Activo,Promedio):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Activo=Activo
        self.Promedio=Promedio




def CargarDatos(ruta):
    with open(ruta) as contenido:
        cuentas = json.load(contenido)
        for cuenta in cuentas:
            print('----------------------------------------------------------')
            print(cuenta)
            print(cuenta.get('nombre'))
            print(cuenta.get('edad'))
            print(cuenta.get('activo'))
            print(cuenta.get('promedio'))
            a = Dato(cuenta.get('nombre'),cuenta.get('edad'),cuenta.get('activo'),cuenta.get('promedio'))
            Lista.append(a)
            print('----------------------------------------------------------')


def Cargar(rutas):
    print(rutas)
    cadenas=rutas.split(',')
    for ruta in cadenas:
        CargarDatos(ruta)

def menu():
    ciclo=True
    while(ciclo):
        ingreso = input("ingrese comando: ")
        cadena=ingreso.lower()
        comando=cadena.split()
        if comando[0] == 'cargar':
            Cargar(comando[1])
        elif comando[0]=='salir':
            ciclo=False

        else :
            print('COMANDO INCORRECTO')
            print()


menu()

