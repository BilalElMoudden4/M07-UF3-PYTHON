'''
#Ejercicio 1:
print("Hello World")

'''


'''
#Ejercicio 2:

numero1 = int(input("Introduce un numero:   "))
numero2 = int(input("Introduce otro numero:   "))

print("La suma es: " + str(numero1 + numero2))

if (numero1 > numero2):
    print(str(numero1) + " es mas grande que " + str(numero2))
else:
    print(str(numero2) + " es mas grande que " + str(numero1))

'''


'''

#Ejercicio 3
frase = input("Introduce una frase:   ")
fraseSinEspacios = frase.replace(" ", "")
print(fraseSinEspacios)

'''


'''


#Ejercicio 4
numeros = 1  

while numeros <= 500:
    if numeros % 2 != 0:  
        print(numeros)
    numeros += 1

    
'''


'''

#Ejercicio5

valorDecimal = float(input("Introduce un valor decimal en €: "))
IVA = float(input("Introduce el valor del IVA, puede ser 4%, 10%, o 21%: "))

# Calcular el valor del IVA aplicado
valorIVA = valorDecimal * (IVA / 100)

# Calcular el valor final sumando el valor original y el IVA
valorFinal = valorDecimal + valorIVA

print("El valor decimal que has introducido es: " + str(valorDecimal))
print("El valor del IVA que has introducido es: " + str(IVA) + "%")
print("El resultado del valor que has introducido más el IVA es: " + str(valorFinal))

'''



'''

#Ejercicio 6

palabras = input("Introduce 2 o 3 palabras:   ")

npalabras = palabras.split()

if ( 2 <= len(npalabras) <= 3):
    for palabras in npalabras:
        longitud = len(palabras)
        primerCaracter = palabras[0]
        ultimoCaracter = palabras[-1]
        print(f"Palabra: {palabras}, Longitud: {longitud}, Primer carácter: {primerCaracter}, Último carácter: {ultimoCaracter}")
else:
    print("Por favor, introduce exactamente 2 o 3 palabras.")

'''

#Ejercicio 7

palabra = str(input("Escribe una palabra para ver si es palindroma o no:   "))

palabraInvertida = palabra[::-1]

if (palabra == palabraInvertida):
    print(str(palabra) + " es palindromo")
else:
    print(str(palabra) + " no es palindromo")

























