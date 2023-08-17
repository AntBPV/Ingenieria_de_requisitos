#Antonio Benjamin Parra Velasquez [850127]
#Ingenieria de requisitos
import os
import json

print("Ejercicio 2: Caso FAndroid")

#inicio definicion de funciones
def guardar_datos(array,name,passw,num,m_exp,y_exp,verif):
    array['name']=name
    array['password']=passw
    array['num_tarjeta']=num
    array['ven_tarjeta']=[m_exp,y_exp]
    array['cod_tarjeta']=verif
    array['points']=int(0)
    with open ('user.json','w') as f:
        json.dump(array, f, indent=2)

def cambiar_usuario(array,name):
    array['name']=name
    with open('user.json','w') as f:
        json.dump(array,f,indent=2)
def cambiar_passw(array,passw):
    array['password']=passw
    with open('user.json','w') as f:
        json.dump(array,f,indent=2)

def cambiar_tarjeta(array,mark,num,m_exp,y_exp,verif):
    match mark:
        case 1:
            array['marca']="BBVA"
        case 2:
            array['marca']="Bancolombia"
        case 3:
            array['marca']="Davivienda"
        case 4:
            array['marca']="AV villas"
    array['num_tarjeta']=num
    array['ven_tarjeta']=[m_exp,y_exp]
    array['cod_tarjeta']=verif
    with open('user.json','w') as f:
        json.dump(array,f,indent=2)

def comprar(array_compra,array_datos,opcion):
    match opcion:
        case 1:
            print("Se realizo un cargo de: $",array_compra[1]['precio']," a la tarjeta de numero ",array_datos['num_tarjeta'])
            print("Has ganado ",array_compra[1]['puntaje']," puntos!")
            array_datos['points']=array_datos['points']+array_compra[1]['puntaje']
        case 2:
            print("Se realizo un cargo de: $",array_compra[2]['precio']," a la tarjeta de numero ",array_datos['num_tarjeta'])
            print("Has ganado ",array_compra[2]['puntaje']," puntos!")
            array_datos['points']=array_datos['points']+array_compra[2]['puntaje']
        case 3:
            print("Se realizo un cargo de: $",array_compra[3]['precio']," a la tarjeta de numero ",array_datos['num_tarjeta'])
            print("Has ganado ",array_compra[3]['puntaje']," puntos!")
            array_datos['points']=array_datos['points']+array_compra[3]['puntaje']
    with open('user.json','w') as f:
        json.dump(array_datos,f,indent=2)

def canjear(array_compra,array_datos,opcion):
    match opcion:
        case 1:
            if array_datos['points']<array_compra[1]:
                print("No tienes suficientes puntos para canjear.")
                return
            print("Has canjeado el premio por ",array_compra[1]," puntos")
            array_datos['points']=array_datos['points']-array_compra[1]
        case 2:
            if array_datos['points']<array_compra[2]:
                print("No tienes suficientes puntos para canjear.")
                return
            print("Has canjeado el premio por ",array_compra[2]," puntos")
            array_datos['points']=array_datos['points']-array_compra[2]
        case 3:
            if array_datos['points']<array_compra[3]:
                print("No tienes suficientes puntos para canjear.")
                return
            print("Has canjeado el premio por ",array_compra[3]," puntos")
            array_datos['points']=array_datos['points']-array_compra[3]
        case 4:
            if array_datos['points']<array_compra[4]:
                print("No tienes suficientes puntos para canjear.")
                return
            print("Has canjeado el premio por ",array_compra[4]," puntos")
            array_datos['points']=array_datos['points']-array_compra[4]
        case 5:
            if array_datos['points']<array_compra[5]:
                print("No tienes suficientes puntos para canjear.")
                return
            print("Has canjeado el premio por ",array_compra[5]," puntos")
            array_datos['points']=array_datos['points']-array_compra[5]
    print("Te quedan: ",array_datos['points']," puntos")
    with open('user.json','w') as f:
        json.dump(array_datos,f,indent=2)
            
#fin definicion de funciones

#incio del codigo del programa
user = {}
salida = bool(False)
while salida == False:
    print("")
    print("Ingrese el numero de la accion deseada: ")
    print("1. Iniciar sesion")
    print("2. Crear cuenta")
    print("3. Salir del programa")
    opcion_home = int(input())
    match opcion_home:
        case 1: #loop para el inicio de sesion e ingreso a la tienda y opciones de informacion de la cuenta
            input("Presione ENTER para continuar")
            os.system('cls')
            with open('user.json','r') as f:
                load_user = json.load(f)
            sign_in = bool(False)
            while sign_in == False:
                sign_name = input("Por favor ingrese su nombre de usuario: ")
                sign_password = input("Por favor ingrese su contraseña: ")
                if sign_name != load_user['name'] or sign_password!=load_user['password']:
                    print("Usuario o contraseña incorrectos...")
                if sign_name==load_user['name'] and sign_password==load_user['password']:
                    sign_in=True
            input("Presione ENTER para continuar")
            os.system('cls')
            store_page = bool(False)
            while store_page == False:
                print("Que desea hacer?")
                print("1. Comprar aplicaciones")
                print("2. Canejar premios")
                print("3. Modificar cuenta")
                print("4. Regresar al menu principal")
                opcion_store=int(input())
                match opcion_store:
                    case 1:
                        print("Se van a mostrar una serie de productos.")
                        tienda={
                            1:{
                                "precio": 30000,
                                "puntaje": 200
                            },
                            2:{
                                "precio": 55000,
                                "puntaje": 420
                            },
                            3:{
                                "precio": 25000,
                                "puntaje": 100
                            }
                        }
                        print("Elija el de su preferencia: ")
                        print("1. Whatsapp plus .....$",tienda[1]['precio'])
                        print("2. Twitter Blue.....$",tienda[2]['precio'])
                        print("3. Youtube premium.....$",tienda[3]['precio'])
                        opcion_product=int(input())
                        comprar(tienda,load_user,opcion_product)
                        input("Presiona ENTER para continuar")
                        os.system('cls')
                    case 2:
                        premios={
                            1: 30,
                            2: 100,
                            3: 45,
                            4: 800,
                            5: 250,
                        }
                        print("Se van a mostrar los premios canjeables")
                        print("Elija el de su preferencia: ")
                        print("1. Usb 10 gigas .....",premios[1])
                        print("2. Audifonos con cable .....",premios[2])
                        print("3. Powerbank .....",premios[3])
                        print("4. Memoria externa .....",premios[4])
                        print("5. Mouse logitech .....",premios[5])
                        opcion_premio=int(input())
                        canjear(premios,load_user,opcion_premio)
                        input("Presione ENTER para continuar")
                        os.system('cls')
                    case 3:
                        os.system('cls')
                        print("MODIFICACION DE DATOS")
                        print("1. Cambiar usuario")
                        print("2. Cambiar contraseña")
                        print("3. Cambiar datos de tarjeta")
                        opcion_modif = int(input())
                        match opcion_modif:
                            case 1:
                                new_name = input("Ingrese su nuevo nombre de usuario: ")
                                cambiar_usuario(load_user,new_name)    
                            case 2:
                                new_passw = input("Ingrese su nueva contraseña: ")
                                cambiar_passw(load_user,new_passw)
                            case 3:
                                print("Siga los pasos indicados")
                                print("Indique con el numero correspondiente la marca o banco de su tarjeta: ")
                                print("1. BBVA")
                                print("2. Bancolombia")
                                print("3. Davivienda")
                                print("4. AV villas")
                                marca_tarjeta=int(input())
                                num_tarjeta=int(input("Ingrese el numero de la tarjeta: "))
                                mnth_tarjeta, yr_tarjeta = input("Por favor ingrese mes y año de vencimiento SEPARADOS POR UN ESPACIO: ").split()
                                cod_tarjeta = int(input("Por favor ingrese el codigo de verificacion de la tarjeta: "))
                                cambiar_tarjeta(load_user,marca_tarjeta,num_tarjeta,mnth_tarjeta,yr_tarjeta,cod_tarjeta)
                    case 4:
                        store_page=True
                        os.system('cls')
            
        case 2: #loop de registro de informacion a almacenar en el archivo .json
            input("Presione ENTER para continuar")
            os.system('cls')
            reg_name = input("Por favor ingrese su nombre de usuario: ")
            reg_password= input("Por favor ingrese su contraseña: ")
            os.system('cls')
            
            print("Debe ingresar obligatoriamente la informacion de su tarjeta de credito o debito para continuar: ")
            print("Indique con el numero correspondiente la marca o banco de su tarjeta: ")
            print("1. BBVA")
            print("2. Bancolombia")
            print("3. Davivienda")
            print("4. AV villas")
            marca_tarjeta = int(input())
            match marca_tarjeta:
                case 1:
                    user['marca']="BBVA"
                case 2:
                    user['marca']="Bancolombia"
                case 3:
                    user['marca']="Davivienda"
                case 4:
                    user['marca']="AV villas"
            print("")
            num_tarjeta = int(input("Por favor ingrese el numero de su tarjeta: "))
            mnth_tarjeta, yr_tarjeta = input("Por favor ingrese mes y año de vencimiento SEPARADOS POR UN ESPACIO: ").split()
            cod_tarjeta = int(input("Por favor ingrese el codigo de verificacion de la tarjeta: "))
            
            guardar_datos(user,reg_name,reg_password,num_tarjeta,mnth_tarjeta,yr_tarjeta,cod_tarjeta)
            
            print("****************************")
            print("*CUENTA CREADA EXITOSAMENTE*")
            print("****************************")
            input("Presione ENTER para continuar")
            os.system('cls')
        case 3: #Opcion de salida, finaliza el programa
            salida = True
        case _: #mensaje de error
            print("ERROR: opcion no valida")
            input("Presione ENTER para continuar")
            os.system('cls')
#fin del programa