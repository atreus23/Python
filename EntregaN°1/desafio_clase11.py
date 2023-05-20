import json
import os

def registro():
    Nombre = input('Ingrese su nombre: ')
    Contrasenia = input('Ingrese su contraseña: ')
    if os.path.exists('datos.json'):
        Lec = open('datos.json', 'r')
        BaseDatos = dict(json.load(Lec))
        Lec.close()
        if Nombre in BaseDatos:
            return print(f'{Nombre} ya esta registrado, inicie sesión')
        else:
            AddData = {Nombre: Contrasenia}
            BaseDatos.update(AddData)
            Esc = open('datos.json', 'w')
            json.dump(BaseDatos, Esc, indent=4)
            Esc.close()
            return print(f'{Nombre} su registro fue exitoso')
    else:
        Registro = {Nombre: Contrasenia}
        Esc = open('datos.json', 'w')
        json.dump(Registro, Esc, indent=4)
        Esc.close()
        return print(f'{Nombre} su registro fue exitoso')

def InicioDeSesion():
    Nombre = input('Ingrese su nombre: ')
    Contrasenia = input('Ingrese su contraseña: ')
    Lec = open('datos.json', 'r')
    BaseDatos = dict(json.load(Lec))
    Lec.close()
    lista = list(BaseDatos.keys())
    if lista.count(Nombre) == 1:
        if BaseDatos[Nombre] == Contrasenia:
            return print(f'{Nombre} bienvenido.')
        else:
            return print('Contraseña incorrecta')
    else:
        return print('Usuario no registrado')
            
def Datos():
    if os.path.exists('datos.json'):
        try:
            Lec = open('datos.json', 'r')
            BaseDatos = dict(json.load(Lec))
            Lec.close()
            for listausuario in BaseDatos:
                print(listausuario)
        except:
            print('No hay usuario registrado')
    else:
        print('No hay usuario registrado')
    
menu = True

while menu:
    print('''
          Opción 1: Iniciar sesión
          Opción 2: Registrarse
          Opción 3: Ver datos
          Opción 4: Salir          
          ''')
    try:
        Opcion = int(input('Elija una opción: '))
        if Opcion == 1:
            InicioDeSesion()
        elif Opcion == 2:
            registro()
        elif Opcion == 3:
            Datos()
        elif Opcion == 4:
            print('Hasta luego')
            menu = False
        else: 
            print('Opción invalida')
    except:
        print('Ingrese un número')