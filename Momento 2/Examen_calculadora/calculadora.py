#Ingenieria_de_Requisitos
#Antonio Benjamin Parra Velasquez [850127]
#Examen calculadora
import os

print("Calculadora basica")

print("Bienvenido a la calculadora basica en lenguaje Python.")
print("A continuacion se le pediran dos valores enteros para ser calculados.")
input("Presione ENTER para poder continuar")
os.system('cls')
valor_1=0
valor_2=0
resultado=0

def sumar(num1, num2, resultado):
    num1 = int(input("Por favor ingrese un numero: "))
    num2 = int(input("Por favor ingrese otro numero: "))
    resultado = num1 + num2
    print("El resultado de la suma de ",num1,"+",num2," es: ",resultado)

def restar(num1, num2, resultado):
    num1 = int(input("Por favor ingrese un numero: "))
    num2 = int(input("Por favor ingrese otro numero: "))
    resultado = num1 - num2
    print("El resultado de la resta de ",num1,"-",num2," es: ",resultado)

def multiplicar(num1, num2, resultado):
    num1 = int(input("Por favor ingrese un numero: "))
    num2 = int(input("Por favor ingrese otro numero: "))
    resultado = num1 * num2
    print("El resultado de la multiplicacion de ",num1,"x",num2," es: ",resultado)

def dividir(num1, num2, resultado):
    num1 = int(input("Por favor ingrese un numero: "))
    num2 = int(input("Por favor ingrese otro numero: "))
    resultado = num1 / num2
    print("El resultado de la division de ",num1,"/",num2," es: ",resultado)


loop = 0
while loop!=1:
    print("Por favor ingrese la opcion deseada para calcular los dos valores ingresados: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=int(input("Ingrese la accion deseada segun su numero de la lista: "))
    match opcion:
        case 1:
            sumar(valor_1,valor_2,resultado)
            input("Presione ENTER para poder continuar")
            os.system('cls')
        case 2:
            restar(valor_1,valor_2,resultado)
            input("Presione ENTER para poder continuar")
            os.system('cls')
        case 3:
            multiplicar(valor_1,valor_2,resultado)
            input("Presione ENTER para poder continuar")
            os.system('cls')
        case 4:
            dividir(valor_1,valor_2,resultado)
            input("Presione ENTER para poder continuar")
            os.system('cls')
        case 5:
            loop=1