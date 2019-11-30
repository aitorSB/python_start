
# Ejecutar el fichero en consola

> python  ./start.py

# Abrir la consola de python

>python 

>py

## Salir de la consola

>exit()

# Imprimir

```py
print("Hello, World!")
```

# Concatenación de elementos

```py
print("Hello, " + "World! " + "concatenacion") 
```

## Error en la concatenación de variables

> No puedes concatenar una variable tipo int con una tipo string

```py
x_int = 5
y_string = "John"
print(x_int + y_string) #ERROR
```

# Comentarios

> #Esto es un comentario de una linea.

```py
#Comentario
print("Hello, World!") #Esto es un comentario
```

> """ comentario en más de una linea """

```py
"""
esto es un comentario en 
diferentes lineas
"""
````

# Indentación

```py
if 5 > 2:
  print("Five is greater than two!")
```

# Variables

```py
x = 5

# Las variables string puedes ser declaradas con comillas simples o dobles
y = "Hellow, World!"

print(y)
```

# Forma de dar valor a las variables

```py
x1, y2 , z3 = "pera", "manzana", "platano"

print(x1)
print(y2)
print(z3)

print(x1 + y2 + z3)
```

# Suma de variables

```py
x1 = "pera"
y2 = "manzana"
xx = x1 + " " + y2

print(xx) # output: pera manzana

numero1 = 1
numero2 = 2

numero_final = numero1 + numero2 

print(numero_final) # output = 3
```

# Obtener tipos de variables

```py
tipovar = 'Hello World!'
print(type(tipovar))
```

# Tipos de variables numéricas

```py
num1 = 1 #int
num2 = 1.1 #float
num3 = 1j #complex  j --> parte imaginaria

print(type(num3))
```

# Conversión de datos

> int(x)

> float(y)

> complex(z)

```py
stringA = '1'
intA = 2

sum = int(stringA) + intA
print(sum)
```
# Random

```py
import random

print(random.randrange(1,100)) 
```

# Obtener caracter de una cadena

```py
a = "Hello, World!"
print(a[4])
```

## Obtener un rango de caracteres de una cadena

```py
b = "Hello, World!"
print(b[2:5])
```
> Rango empezando desde el final

```py
b = "Hello, World!"
print(b[-5:-2])
```

# Longitud de una cadena

```py
a = "Hello, World!"
print(len(a))
```

# Eliminar espacios exteriores 

```py
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  trim()
```

# Convertir a mayúsculas y minúsculas 

```py
a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())
```

# Reemplazar caracteres

```py
a = "Hello, World!"
print(a.replace("H", "J"))
```

# Separar cadenas split devuelve una lista

```py
a = "Hello, World!"
cadenaSeparada = a.split(",")
print(cadenaSeparada) # returns ['Hello', ' World!'] 
print(cadenaSeparada[0]) # return Hello
print(type(cadenaSeparada)) # list
```

# Buscar en cadena 

```py
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)  
```