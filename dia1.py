print(2/2)
print(6+9)
print(2+1)
print('hola mundo') #parentesis para ejecutar operaciones
print('hola man')
print('hola'*3)
print("mira un poco ") # comilla para texto
a = 4 # el =es para guardar asignar u guardar valores
b = 6
print(a+b)
print(a, b) #la coma para separar elementos
#ejercicio. crear una variable nombre y edad con sus nombres y edad e imprimir:
nombre= "Gabiel Alejandro"
año= 31
hobby= "paintball"
print("hola me llamo", nombre, "y tengo", año, "  años de edad","y mi hobby es el ", hobby)

lista_vacia= []
listax = [1,2,3,4] #conjunto de variables o valores o definiciones individuales
#ejer. crear una lista de datos que en el l primer lugar este tu nombre
# en la segunda posicio este tu edad.
#imprimir "hola me llamo_____, y tengo____ años"
alumnos= [nombre, año, hobby] 
print ("hola me llamo", alumnos[0],"y tengo", alumnos[1], "mi hobby es el", alumnos[2])
alumnos[2]= "voley" #para cambiar el valor de la variable es seleccionar de la lista la variable y cambiar el valor
print ("hola me llamo", alumnos[0],"y tengo", alumnos[1], "mi hobby es el", alumnos[2])
alumnos.append("emprendedor") #usar append para agregar 1 elemnto a la lista 
#agregar 1 profesion y hobby a la la lista previamente creada
print ("hola me llamo", alumnos[0],"y tengo", alumnos[1], "mi hobby es el", alumnos[2],"y mi profesion es ser", alumnos[3])
alumnos.pop() #para eliminar el ultimo elemento de la lista "pop"
print(alumnos) 
# len=> lenght es una funcion que indica la cantidad de elementos
print(len(alumnos))
#ejer. obtener la dimencion de la lista de datos e imprimir
#la lista de datos tien_______ elementos'
print("la listad de alumnos tiene", len(alumnos) , "elementos")
# jer. imprimir el ultimo elemneto de una lista que no sabemo cuantos elemntos tiene 
lista_larga= ["jose", "neide", "carlos", "pepe", "carola", "apache", "gabriel", "jorge", "sime", "adri", "lolo", "pablo", "diana"]
print(len(lista_larga))
posicion=len(lista_larga)-1 #variable nueva donde indica cual (con len )es la ultima posicion de la lista menos 1 por que empiza de 0

print(lista_larga[posicion]) 
#### bucles/loops/ciclos/interaciones######
lista_temas=["variables", "lista","tipos de datos"]
for concepto in lista_temas:
    print("hoy aprendi", concepto)
    print("que gusto")
print("esto es lo que aprendi hoy")
for variable_for in lista_temas:
    #bloque de codigo
    print("esto se repite")
print("esto no se repite")

#ejer. recorrer una lista con for e imprimir en cada ciclo el elemento con 3 signos de admiracion (variables!!!) y fuera del bucle FIN!!!

for concepto in lista_larga: # para bucles repetitivos de variables de una lista
    print("compñeros!!!", concepto)
    print("buena onda")
print("fin!!")

for x in range(1 ,101): #para aumentar elemntos e este caso 7 vces ha upei
    print("ha upei", x) #repetir la x es PARA ENUMERAR LAS VECES QUE SE REPITE 








