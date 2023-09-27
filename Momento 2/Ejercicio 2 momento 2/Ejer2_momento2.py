#Antonio Benjamin Parra Velasquez [850127]
#Ingenieria de requisitos

import os
import json
import os.path
import random
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

print("Ejercicio 2: Diagramas de clase.")

save=os.path.exists('data.json')

if save==False:
    carga={
        "cliente": {
            "codigo":[],
            "nombre":[],
            "DNI":[],
            "direccion":[],
            "telefono":[],
            "tarjeta":{
                "numero":[],
                "cod_verificacion":[],
                "fecha_exp":[]
            }
        },
        "agencia":{
            "nombre":["Carros pepe"],
            "direccion":["cra 23 #13-19"],
            "telefono":["314 8842790"]
        },
        "coche":{
            "marca":["Ford","Mustang","Honda"],
            "disponibilidad":[False,True,True],
            "matricula":["CNA-891","AZN-342","BOF-420"],
            "modelo":["2020","2018","2021"],
            "color":["Rojo","Gris","Negro"],
            "precio":[600000,450000,200000],
            "garaje":{
                "codigo":[9692],
                "capacidad_max":[3],
                "direccion":["cra 43 #17-23"]
            }
        },
        "reserva":{
            "fecha_inicio":[],
            "fecha_fin":[],
            "codigo":[],
            "entrega":[],
            "coche":{
                "marca":[],
                "matricula":[],
                "modelo":[],
                "color":[],
                "precio":[],
                "garaje":{
                    "codigo":[9692],
                    "capacidad_max":[3],
                    "direccion":["cra 43 #17-23"]
                }
            }
        }
    }
    with open('data.json','w') as f:
        json.dump(carga,f,indent=2)
with open('data.json','r') as f:
    datos=json.load(f)
print("Bienvenido, siga los pasos indicados para realizar una reserva: ")

def guardar_cliente(array,nombre,dni,direccion,telefono,numero,codigo,fecha):
    array['cliente']['codigo'].append(random.randint(0,1000000))
    array['cliente']['nombre'].append(nombre)
    array['cliente']['DNI'].append(dni)
    array['cliente']['direccion'].append(direccion)
    array['cliente']['telefono'].append(telefono)
    array['cliente']['tarjeta']['numero'].append(numero)
    array['cliente']['tarjeta']['cod_verificacion'].append(codigo)
    array['cliente']['tarjeta']['fecha_exp'].append(fecha)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)

def guardar_reserva(array,fecha_inicio,fecha_fin):
    array['reserva']['codigo'].append(random.randint(0,1000000))
    array['reserva']['fecha_inicio'].append(fecha_inicio)
    array['reserva']['fecha_fin'].append(fecha_fin)
    array['reserva']['entrega'].append(False)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)
        
def guardar_coche(array,marca,matricula,modelo,color,precio):
    array['reserva']['coche']['marca'].append(marca)
    array['reserva']['coche']['matricula'].append(matricula)
    array['reserva']['coche']['modelo'].append(modelo)
    array['reserva']['coche']['color'].append(color)
    array['reserva']['coche']['precio'].append(precio)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)
        
def borrar_datos(array,n):
    array['cliente']['codigo'].pop(n)
    array['cliente']['nombre'].pop(n)
    array['cliente']['DNI'].pop(n)
    array['cliente']['direccion'].pop(n)
    array['cliente']['telefono'].pop(n)
    array['cliente']['tarjeta']['numero'].pop(n)
    array['cliente']['tarjeta']['cod_verificacion'].pop(n)
    array['cliente']['tarjeta']['fecha_exp'].pop(n)
    array['reserva']['codigo'].pop(n)
    array['reserva']['fecha_inicio'].pop(n)
    array['reserva']['fecha_fin'].pop(n)
    array['reserva']['entrega'].pop(n)
    for i in array['reserva']['coche']['marca']:
        array['reserva']['coche']['marca'].remove(i)
    for i in array['reserva']['coche']['matricula']:
        array['reserva']['coche']['matricula'].remove(i)
    for i in array['reserva']['coche']['modelo']:
        array['reserva']['coche']['modelo'].remove(i)
    for i in array['reserva']['coche']['color']:
        array['reserva']['coche']['color'].remove(i)
    for i in array['reserva']['coche']['precio']:
        array['reserva']['coche']['precio'].remove(i)
    with open('data.json','w') as f:
        json.dump(array,f,indent=2)
    
menu_opcion=0
while menu_opcion!=4:
    print("Seleccione su caso: ")
    print("1. Realizar reserva")
    print("2. Consultar reserva")
    print("3. Cancelar reserva")
    print("4. Salir del programa")
    menu_opcion=int(input())
    os.system('cls')
    match menu_opcion :
        case 1:
            print("Para realizar una reserva por favor siga los pasos indicados: ")
            nom_client=input("Por favor ingrese su nombre: ")
            dni_client=int(input("Por favor ingrese el numero de su DNI: "))
            dir_client=input("Por favor ingrese su direccion: ")
            tel_client=input("Por favor ingrese su numero de telefono: ")
            input("Presione enter para continuar...")
            os.system('cls')
            print("Por favor ingrese los datos de su tarjeta ")
            num_tarjeta=int(input("Por favor ingrese el numero de su tarjeta: "))
            codverif_tarjeta=int(input("Por favor ingrese el codigo de verificacion de su tarjeta: "))
            fecha_exp=input("Por favor ingrese la fecha de vencimiento de su tarjeta (Separe año y mes con el simbolo /): ")
            fecha=datetime.strptime(fecha_exp, "%Y/%m")
            ts_exp=fecha.timestamp()
            guardar_cliente(datos,nom_client,dni_client,dir_client,
                            tel_client,num_tarjeta,codverif_tarjeta,ts_exp)
            input("Presione enter para continuar...")
            os.system('cls')
            
            fecha_inicio=datetime.now()
            ts_inicio=fecha_inicio.timestamp()
            fecha_final= datetime.now() + relativedelta(months=+3)
            ts_final=fecha_final.timestamp()
            guardar_reserva(datos,ts_inicio,ts_final)
            
            print("Seleccione el carro de su preferencia: ")
            loop_coche=0
            while loop_coche!=1:
                loop_disponibilidad=0
                while loop_disponibilidad!=1:
                    n=0
                    for i in datos['coche']['marca']:
                        print(n+1,".",i,".......",datos['coche']['color'][n])
                        n=n+1
                    n=int(input("ingrese el numero acorde al coche de su preferencia: "))
                    marca=datos['coche']['marca'][n-1]
                    disponibilidad=datos['coche']['disponibilidad'][n-1]
                    matricula=datos['coche']['matricula'][n-1]
                    modelo=datos['coche']['modelo'][n-1]
                    color=datos['coche']['color'][n-1]
                    precio=datos['coche']['precio'][n-1]
                    
                    if disponibilidad==False:
                        print("El coche seleccionado no se encuentra disponible, pruebe con otro.")
                    else:
                        guardar_coche(datos,marca,matricula,modelo,color,precio)
                        print("Coche guardado exitosamente...")
                        loop_disponibilidad=1
                print("")
                print("Desea añadir otro coche a su reserva?")
                print("ingrese s (si) o n (no)")
                opcion_coche=input()
                if opcion_coche=='n' or opcion_coche=='N':
                    loop_coche=1
                os.system('cls')
            input("Presione enter para continuar...")
            os.system('cls')
            
            print("***************************")
            print("RESERVA CREADA EXITOSAMENTE")
            print("***************************")
            print("Inicia: ",fecha_inicio)
            print("Termina: ",fecha_final)
            total=0
            for i in datos['reserva']['coche']['precio']:
                total=total+i
            print("Precio total: ",total)
            print("Dirijase a la agencia indicada para proceder con su pago y la entrega de su vehiculo: ")
            print(datos['agencia']['nombre'][0])
            print(datos['agencia']['direccion'][0])
            print("")
            print("El codigo de su reserva es: ",datos['reserva']['codigo'][0])
            input("Presione enter para continuar...")
            os.system('cls')
        case 2:
            print("Por favor ingrese el codigo de su reserva: ")
            cod_reserva=int(input())
            found=datos['reserva']['codigo'].index(cod_reserva)
            fecha_ini_found=datetime.fromtimestamp(datos['reserva']['fecha_inicio'][found])
            fecha_fin_found=datetime.fromtimestamp(datos['reserva']['fecha_fin'][found])
            print("Inicia: ",fecha_ini_found)
            print("Termina: ",fecha_fin_found)
            total=0
            for i in datos['reserva']['coche']['precio']:
                total=total+i
            print("Precio total: ",total)
            if datos['reserva']['entrega']==False:
                print("Su coche aun no se entrega.")
            print("Dirijase a la agencia indicada para proceder con su pago y la entrega de su vehiculo: ")
            print(datos['agencia']['nombre'][0])
            print(datos['agencia']['direccion'][0])
            input("Presione enter para continuar...")
            os.system('cls')
        case 3:
            print("Desea cancelar su reserva? S/N")
            opcion_cancelacion=input()
            if opcion_cancelacion=='s' or opcion_cancelacion=='S':
                print("Por favor ingrese el codigo de su reserva: ")
                cod_reserva=int(input())
                found=datos['reserva']['codigo'].index(cod_reserva)
                borrar_datos(datos,found)
            input("Presione enter para continuar...")
            os.system('cls')