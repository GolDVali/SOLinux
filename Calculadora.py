"""programa que hac5
e operaciones de calculadora"""
numero1=0
numero2=0
opcion=0

def suma(numero1,numero2):
    str(print("la suma de los numeros es: ", numero1+numero2))

    
def resta(numero1,numero2):
    str(print("la resta de los numeros es: ", numero1-numero2))

def multi(numero1,numero2):
    str(print("la multiplicacion de los numeros es: ", numero1*numero2))

def division(numero1,numero2):
    str(print("la division de los numeros es: ", numero1/numero2))

    
numero1=int(input("dame el primer numero "))
numero2=int(input("dame el segundo numero "))

opcion=str(input("elija una operacion a realizar:\n [1]Suma\n [2]Resta\n [3]Multiplicacion\n [4]Dividir\n [0]Salir\n"))

if opcion =="1":
    suma(numero1,numero2)
elif opcion =="2":
    resta(numero1,numero2)
elif opcion =="3":
    multi(numero1,numero2)
elif opcion == "4":
    division(numero1,numero2)
else:
    print("adios")


