#Antonio Benjamin Parra Velasquez [850127]
#Ingenieria de requisitos

import os
import json
import os.path

print("Ejercicio 1: Diagramas de clase.")

save=os.path.exists('data.json')
if save==False:
    carga={
        "empleado":{
            "nombre":[],
            "edad":[],
            "cargo":[],
            "sueldo":[],
            "empresa":[]
        },
        "cliente":{
            "nombre":[],
            "edad":[],
            "telefono":[],
            "empresa":[]
        }
    }
    with open('data.json','w') as f:
        json.dump(carga,f,indent=2)
with open('data.json','r') as f:
    datos=json.load(f)
    
def guardar_empleado(array,nombre,edad,cargo,sueldo,empresa):
    array['empleado']['nombre'].append(nombre)
    array['empleado']['edad'].append(edad)
    array['empleado']['cargo'].append(cargo)
    array['empleado']['sueldo'].append(sueldo)
    array['empleado']['empresa'].append(empresa)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)

def guardar_cliente(array,nombre,edad,telefono,empresa):
    array['cliente']['nombre'].append(nombre)
    array['cliente']['edad'].append(edad)
    array['cliente']['telefono'].append(telefono)
    array['cliente']['empresa'].append(empresa)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)

def mostrar_empleado(array,num):
    print("Nombre: ",array['empleado']['nombre'][num-1])
    print("Edad: ",array['empleado']['edad'][num-1])
    print("Cargo: ",array['empleado']['cargo'][num-1])
    print("Sueldo: ",array['empleado']['sueldo'][num-1])
    print("Empresa en la que trabaja: ",array['empleado']['empresa'][num-1])

def mostrar_cliente(array,num):
    print("Nombre: ",array['cliente']['nombre'][num-1])
    print("Edad: ",array['cliente']['edad'][num-1])
    print("Telefono: ",array['cliente']['telefono'][num-1])
    print("Empresa a la que acudio: ",array['cliente']['empresa'][num-1])

menu_opcion = 0
while menu_opcion!=3:
    print("Bienvenido, por favor ingrese la accion que desea realizar: ")
    print("1. Ingresar datos")
    print("2. Extraer datos")
    print("3. Salir del programa")
    menu_opcion=int(input())
    os.system('cls')
    match menu_opcion:
        case 1:
            print("Por favor seleccione los datos de quien va registrar en el sistema: ")
            print("1. Empleado")
            print("2. Cliente")
            registro_opcion =int(input())
            match registro_opcion:
                case 1:
                    print("A continuacion se le pedira la informacion del empleado a registrar: ")
                    nom_empleado=input("Nombre del empleado: ")
                    edad_empleado=int(input("Edad del empleado: "))
                    cargo_empleado=input("Cargo del empleado: ")
                    sueldo_empleado=int(input("Sueldo del empleado: "))
                    empresa_empleado=input("Empresa en la que trabaja: ")
                    guardar_empleado(datos,nom_empleado,edad_empleado,cargo_empleado,
                                     sueldo_empleado, empresa_empleado)
                    input("Presione ENTER para continuar...")
                    os.system('cls')
                case 2:
                    print("A continuacion se le pedira la informacion del cliente a registar: ")
                    nom_cliente=input("Nombre del cliente: ")
                    edad_cliente=int(input("Edad del cliente: "))
                    telefono=input("Telefono del cliente: ")
                    empresa_cliente=input("Empresa a la que acudio: ")
                    guardar_cliente(datos,nom_cliente,edad_cliente,
                                    telefono, empresa_cliente)
                    input("Presione ENTER para continuar...")
                    os.system('cls') 
        case 2:
            n=0
            print("Por favor seleccione que tipo de datos quiere ver: ")
            print("1. Datos de empleados")
            print("2. Datos de clientes")
            extraccion_opcion=int(input())
            os.system('cls')
            match extraccion_opcion:
                case 1:
                    for i in datos['empleado']['nombre']:
                        print(n+1,". ",i)
                    print("Escoja el empleado a mostrar sus datos: ")
                    n=int(input())
                    mostrar_empleado(datos,n)
                    input("Presione ENTER para continuar...")
                    os.system('cls')
                case 2:
                    for i in datos['cliente']['nombre']:
                        print(n+1,". ",i)
                    print("Escoja el cliente a mostrar sus datos: ")
                    n=int(input())
                    mostrar_cliente(datos,n)
                    input("Presione ENTER para continuar...")
                    os.system('cls')
        case 3:
            print()
        
        case _:
            print("Error")