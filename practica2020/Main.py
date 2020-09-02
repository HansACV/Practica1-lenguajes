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
            a = Dato(cuenta.get('nombre'),cuenta.get('edad'),cuenta.get('activo'),cuenta.get('promedio'))
            Lista.append(a)



def Cargar(rutas):
    cadenas=rutas.split(', ')
    for ruta in cadenas:
        CargarDatos(ruta)
    print("Datos Cargardos correctamente")


def Selccionar(cadena):
    nom=False
    age=False
    dir=False
    prom=False
    separacion = cadena.split('DONDE')
    quitar = separacion[0].replace(' ','')
    if quitar=='*':
        nom = True
        age = True
        dir = True
        prom = True
    else:
        atributos = quitar.split(',')
        for a in atributos:
            if a =='nombre':
                nom=True
            elif a=='edad':
                age=True
            elif a=='activo':
                dir=True
            elif a=='promedio':
                prom=True
            else:
                print('No existe el atributo: '+a)

    if len(separacion)==2:
        restriccion = separacion[1].split('=')
        tipo=restriccion[0].strip()
        condicion=restriccion[1].replace('"','').strip()
        if tipo=='nombre':
            impresion = ''
            for a in Lista:
                if a.Nombre==condicion:
                    if nom == True:
                        impresion = impresion + " Nombre: " + a.Nombre
                    if age == True:
                        ed = str(a.Edad)
                        impresion = impresion + " Edad: " + ed
                    if dir == True:
                        if a.Activo == True:
                            impresion = impresion + " Activo"
                        elif a.Activo == False:
                            impresion = impresion + " Inactivo"
                    if prom == True:
                        p = str(a.Promedio)
                        impresion = impresion + " Promedio: " + p
                    print(impresion)
                    impresion=""
        if tipo=='edad':
            impresion = ''
            con=int(condicion)
            for a in Lista:
                if a.Edad==con:
                    if nom == True:
                        impresion = impresion + " Nombre: " + a.Nombre
                    if age == True:
                        ed = str(a.Edad)
                        impresion = impresion + " Edad: " + ed
                    if dir == True:
                        if a.Activo == True:
                            impresion = impresion + " Activo"
                        elif a.Activo == False:
                            impresion = impresion + " Inactivo"
                    if prom == True:
                        p = str(a.Promedio)
                        impresion = impresion + " Promedio: " + p
                    print(impresion)
                    impresion=""

        if tipo=='promedio':
            impresion = ''
            con=float(condicion)
            for a in Lista:
                if a.Promedio==con:
                    if nom == True:
                        impresion = impresion + " Nombre: " + a.Nombre
                    if age == True:
                        ed = str(a.Edad)
                        impresion = impresion + " Edad: " + ed
                    if dir == True:
                        if a.Activo == True:
                            impresion = impresion + " Activo"
                        elif a.Activo == False:
                            impresion = impresion + " Inactivo"
                    if prom == True:
                        p = str(a.Promedio)
                        impresion = impresion + " Promedio: " + p
                    print(impresion)
                    impresion=""

    elif len(separacion)==1:
        impresion=''
        for a in Lista:
            if nom==True:
                impresion=impresion+" Nombre: "+a.Nombre
            if age==True:
                ed=str(a.Edad)
                impresion=impresion+" Edad: "+ed
            if dir==True:
                if a.Activo==True:
                    impresion=impresion+" Activo"
                elif a.Activo==False:
                    impresion=impresion+" Inactivo"
            if prom==True:
                p=str(a.Promedio)
                impresion=impresion+" Promedio: "+p

            print(impresion)
            impresion=""



def menu():
    ciclo=True
    while(ciclo):
        ingreso = input("ingrese comando: ")
        comando=ingreso.split(maxsplit=1)
        com=comando[0].lower()
        if com == 'cargar':
            Cargar(comando[1])
        elif com == 'seleccionar':
            Selccionar(comando[1])
        elif com == 'salir':
            ciclo=False

        else :
            print('COMANDO INCORRECTO')
            print()


menu()

