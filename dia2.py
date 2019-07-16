# tipo de datos/cadena/str de texto
" esto es un string"
#tipo de datos interger/entero/int
105
#lista
[] #lista vacia
["gabriel", 33, "pizzero"] #lista de 3 elementos
# variables
nombre= "gabriel"
edad= 30 + 1
edad_mal= "30+1" # se lee como texto con las comillas
variable_lista= ["hola", nombre, 89]
#acceder a un elemnto de la lista
print(variable_lista[0], edad, variable_lista[2])
#acciones/operaciones sobre listas
variable_lista.append("paintball") #agregar elemento a la lista
variable_lista.pop() #eliminar elemento
variable_lista[2]= 87 #para modificar elemntos dentro de la lista en una posicion especifica
print(variable_lista)


# bucles /loop/ciclos
for loquesea in variable_lista:
     print(loquesea)
# imprimir los numeros del 1 al 10
for cualquiercosa in range(1, 11):  # agregar 1 por que la cuenrta va del 0,1,2...
    print(cualquiercosa)

# impromir el ultimo elemento de una lista sin saber cuantos elementos tiene, solicion general
otra_lista = [ "hola que tal", "chau", 7]
otra_lista.append("AAA")

#solucon paso por paso
dim_lista = len(otra_lista)
print("la dimension de otra lista es", dim_lista)
indice_del_ultimo = dim_lista - 1
print("el indice del ultimo elemnto es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])



# esto es quivalente
for numero in range(1,11):
    print(numero)

# a esto 
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
# imprimir hola 10 veces 
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", numero) # imprimir numero es opcional



# desafio
# imprimir el nro de resultado de la suma de lso nrumeros de 1 al 10
# -> 55 resultado
# esto seria para crear un acumulador
challenge= [1,2,3,4,5,6,7,8,9,10] #se crea una lista
a= 0              # se crea una variable base
for x in challenge: # se crea un ciclo que corre  en cada uno de los elementos de la lista challenge
    a=a+x          # se van acumulando (recursividad se va usand el valor de "a" a si mismo )
print(a)



sumatoria=0
for valor in range(1,11):
    sumatoria= sumatoria + valor
print(sumatoria)





############# FUNCIONES ###################



def suma(num1, num2):
    resultado= num1, num2
    return resultado

# equivalente al de arriba
def suma2(num1, num2):
    return num1 + num2

print(suma(5, 10))
resul = suma(5,8)
print(resul)  


# crear una funcion resta, que reciba como parametro dos numeros y retorne la resta de esos numeros
# luego llamr e imprimir el resultado

def resta(num1, num2):
    resultado= num1-num2
    return resultado
print(resta(9,2))
print(resta(15,2))


# crear una funcion saludo2 que reciba como parametro nombre edad e imprimir "hola soy____y tengo____años"
# llamar varias veces a la funcion con distintos valores
# retornar es algo opcional
 
def saludo2(nombre, edad):
    print("hola soy", nombre,"y tengo", edad)
saludo2("Gabriel", 31)
saludo2("juan", 22)
saludo2("sime", 23)
saludo2("juana", 18)
# crear una funcion suma_lista que reciba como argumento una lista de numerosy retprne la suma de sus elementos
# pista usar acumulador


def suma_lista(lista1):
    sumatoria=0
    for valor in lista1:
        sumatoria= sumatoria + valor
    return sumatoria
resultado = suma_lista([1,2,3,4,5])
print(resultado)

# eje2 lista al cuadrado
#crear una funcion que reciba una lista de numeros como parametro y retorne una lista con los numeros al cuadrado
#lista_cuadrado(listita)--> [1,4,9,16,25]

def lista_cuadrado(listita):
    lista=[]
    for suma in listita:
        lista.append(suma * suma)
    return lista
cualquiera= [1,4,9,16,25]
print(lista_cuadrado(cualquiera))

# ELIMINAR todos los elemntos de una lista utilizando "for"


grupo5=["N","F1","F2","A"]
for j in range(len(grupo5)):
    grupo5.pop()
print("despues", grupo5)

# cear una funcion suma_cuadrado que reciba una lista de numeros y retorne el valor de las sumas de cada nro al cuadrado
# [1,2,3,4] ---> 1+4+9,16 ---> 30
def suma_cuadrado(listaaa):
    liste= []
    for 
       
    




    
