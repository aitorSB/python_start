#! python3

# *************************************************************************
# imprimir en consola
# *************************************************************************

print("Hello, World!")

## concatenacion de elementos

print("Hello, " + "World! " + "concatenacion") 

# *************************************************************************
# indentacion
# *************************************************************************

if 5 > 2:
    print('5 es mayor que 2')

# *************************************************************************
# variables
# *************************************************************************

x = 5 #variable int
y = "Hello, World!" #variable string comillas dobles
z = 'Hellow, World2!' #variable string comillas simples

print(x)
print(y)
print(z)
    
# distinta forma de dar valor a las variables

x1, y2 , z3 = "pera", "manzana", "platano"

print(x1)
print(y2)
print(z3)

print(x1 + y2 + z3) # output: peramanzaplatano

# suma de variables

xx = x1 + " " + y2

print(xx) # output: pera manzana

numero1 = 1
numero2 = 2

numero_final = numero1 + numero2 

print(numero_final) # output = 3

# Obtener tipos de variables

tipovar = 'Hello World!'
print(type(tipovar))


# Tipos de variables numéricas

num1 = 1 #int
num2 = 1.1 #float
num3 = 1j #complex  j --> parte imaginaria

print(type(num3))

# Conversión de datos

stringA = '1'
intA = 2

sum = int(stringA) + intA
print(sum)

# Random

import random

print(random.randrange(1,100)) 

# Obtener caracter de una cadena

a = "Hello, World!"
print(a[4])

# Obtener un rango de caracteres de una cadena

b = "Hello, World!"
print(b[2:5])

# Rango empezando desde el final

b = "Hello, World!"
print(b[-5:-2])

# Longitud de una cadena

a = "Hello, World!"
print(len(a))

# Eliminar espacios exteriores 

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

# Convertir a mayúsculas y minúsculas 

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

# Reemplazar caracteres

a = "Hello, World!"
print(a.replace("H", "J"))

# Separar cadenas split devuelve una lista

a = "Hello, World!"
cadenaSeparada = a.split(",")
print(cadenaSeparada) # returns ['Hello', ' World!'] 
print(cadenaSeparada[0]) # return Hello
print(type(cadenaSeparada)) # list

# Buscar en una cadena

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #false - true

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)  

# Concatenación mediante format

age = 36
day = 20
year = 123
txt = "My name is John, and I am {} {} {}"
print(txt.format(age, day , year))