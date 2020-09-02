import json
import webbrowser

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

def Maximo(tipo):
    if tipo == 'edad':
        numero=0
        for a in Lista:
            if numero < a.Edad:
                numero=a.Edad
        print('La mayor edad es: '+ str(numero) )
    elif tipo == 'promedio':
        numero=0.0
        for a in Lista:
            if numero<a.Promedio:
                numero=a.Promedio
        print('El mayor promedio es: '+ str(numero))

def Minimo(tipo):
    if tipo == 'edad':
        numero = Lista[0].Edad
        for a in Lista:
            if numero > a.Edad:
                numero=a.Edad
        print('La menor edad es: '+str(numero))
    elif tipo == 'promedio':
        numero = Lista[0].Promedio
        for a in Lista:
            if numero > a.Promedio:
                numero=a.Promedio
        print('El mayor promedio es: '+str(numero))

def Suma(tipo):
    if tipo == 'edad':
        total=0
        for a in Lista:
            total = total+a.Edad
        print('La suma de las edades es: '+str(total))
    elif tipo=='promedio':
        total=0.0
        for a in Lista:
            total = total + a.Promedio
        print('La suma de los promedios es: '+ str(total))

def Reportar(cantidad):
    reporte = open('Reporte.html','w')
    reporte.write('<!DOCTYPE html>\n')
    reporte.write('<html>\n')
    reporte.write('<head>\n')
    reporte.write('     <title>Reporte</title>\n')
    reporte.write('</head>\n')
    reporte.write('<style type="text/css">\n')
    reporte.write('  table, th, td {\n')
    reporte.write('         border: 1px solid black;')
    reporte.write('         border-collapse: collapse;')
    reporte.write('  }')

    reporte.write('</style>\n')
    reporte.write('<body>\n')


    reporte.write('<h1>Reporte</h1>\n')
    reporte.write('<table style="width: 100%">\n')
    reporte.write('<tr> <th>Nombre</th> <th>Edad</th> <th>Promedio</th> <th>Activo</th> </tr>\n')
    n=0
    for a in Lista:
       if n==cantidad:
           break
       else:
           if a.Activo==True:
               reporte.write('<tr> <td>'+a.Nombre+'</td> <td>'+str(a.Edad)+'</td> <td>'+str(a.Promedio)+'</td> <td>True</td> </tr>\n')
           elif a.Activo==False:
               reporte.write('<tr> <td>'+a.Nombre+'</td> <td>'+str(a.Edad)+'</td> <td>'+str(a.Promedio)+'</td> <td>False</td> </tr>\n')
       n=n+1


    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close()

    webbrowser.open_new_tab('Reporte.html')

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
        elif com=='maximo':
            Maximo(comando[1])
        elif com=='minimo':
            Minimo(comando[1])
        elif com=='suma':
            Suma(comando[1])
        elif com=='cuenta':
            print('El total de registros en memoria es: ' + str(len(Lista)))
        elif com=='reportar':
            Reportar(int(comando[1]))
        elif com == 'salir':
            ciclo=False

        else :
            print('COMANDO INCORRECTO')
            print()


menu()

