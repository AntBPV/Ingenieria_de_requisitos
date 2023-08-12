#Antonio Benjamin Parra Velasquez [850127]
#Ingenieria de requisitos
import os

print("Ejercicio 1: Requisitos para expedicion automatica de boletos de tren.")

precio = int(0) #Guardar el precio del destino seleccionado por el usuario.
opcion = str('') #Valor de opcion utilizado a lo largo del programa.
Loop_Seleccion = bool(0) #Este valor, nos permite mantener al usuario en la misma pantalla hasta que seleccione un destino.
Loop_Datos = bool(0) #Este valor, nos permite mantener al usuario en la pantalla de datos personales.
Loop_Validacion = bool(0) #Valor para mantener al usuario en la pantalla de confirmacion.


while Loop_Seleccion != 1 :
    print("Por favor seleccione su destino de la siguiente lista: ")
    print("(Seleccione el numero que aparece en la lista)")
    print("1. Venezuela")
    print("2. Peru")
    print("3. Brasil")
    Dest_seleccion = int(input()) #Nos da el destino que el usuario quiere.
    os.system('cls')
    match Dest_seleccion:
        case 1:
            print("")
            print("Viaje a Venezuela")
            print("Precio: $30000")
            precio = 30000
            print("")
        case 2:
            print("")
            print("Viaje a Peru")
            print("Precio: $45000")
            precio = 45000
            print("")
        case 3:
            print("")
            print("Viaje a Brasil")
            print("Precio: $70000")
            precio = 70000
            print("")
        case _:
            print("")
            print("ERROR: Destino no encontrado.")
            print("")
    if Dest_seleccion==1 or Dest_seleccion==2 or Dest_seleccion==3:
        print("El destino ingresado es correcto?...")
        print("(S/N)")
        opcion = input()
        if opcion=='s' or opcion=='S':
            Loop_Seleccion=1
    os.system('cls')

while Loop_Datos < 1 :
    print("Ingrese los datos para continuar con el proceso.")
    Num_Id = int(input("Ingrese su numero de identificacion o ID: ")) #Identificacion del usuario
    Num_Tarjeta = int(input("Ingrese el numero de su tarjeta: ")) #Tarjeta del usuario
    print("Los datos ingresados son: ")
    print("ID: ",Num_Id)
    print("Tarjeta: ",Num_Tarjeta)
    print("")
    print("Son correctos estos datos? (S/N)")
    opcion = input()
    if opcion == 's' or opcion== 'S':
        Loop_Datos=1
        print("Expediendo su boleto...")
    input("Presione ENTER para continuar...")
    os.system('cls')

match Dest_seleccion:
    case 1:
        print("******************************")
        print("Viaje con destino a Venezuela.")
        print("Cargo de $",precio)
        print("******************************")
    case 2:
        print("*************************")
        print("Viaje con destino a Peru.")
        print("Cargo de $",precio)
        print("*************************")
    case 3:
        print("***************************")
        print("Viaje con destino a Brasil.")
        print("Cargo de $",precio)
        print("***************************")
    
input("Presione ENTER para continuar...")
os.system('cls')
print("Por favor ingrese su numero de ID para validar la transaccion.")

while Loop_Validacion<1:
    Num_confirm = int(input()) #Valor a coincidir con la ID del usuario.
    if Num_confirm==Num_Id:
        print("")
        print("***************************************************************")
        print("Se ha realizado un cargo de $",precio," a la tarjeta vinculada.")
        print("Tarjeta ",Num_Tarjeta)
        print("***************************************************************")
        print("")
        Loop_Validacion=1

print("Finalizando programa...")
input("Presione ENTER para continuar...")

