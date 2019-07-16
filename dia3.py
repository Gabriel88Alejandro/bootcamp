# ejemplo de def y for 



def imprimir_lista(ingredientes, nombre_producto): # ingrdientes es igual a ing_pan
    print("lista de compras de", nombre_producto)
    print("______________")
    for producto in ingredientes: 
        print(producto)




ingr_pan=[ "harina","levadura", "agua", "sal", "azucar"]
imprimir_lista(ingr_pan,"pan")



#---------------------------------------------------------------

######################################condicionales####################################
# == igual
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto
print("CONDICIONALES")
a= 5
# PREGUNTA 1
if a > 3:
    print("Si, a es mayor a 3")
    print("chau")
# PREGUNTA 2
else:
    print("No, no se mayor a 3")
# PREGUNTA 3
if a== 3:
    print(" a es igual a 3")

nota = 60
if nota > 60:
    print("pasaste!!!!!")
else: 
    print("HULE YA")


# EJER. crear una funcion que reciba como parametro una nota de 1 al 100 e imprimir si pasaste o no !!


def notas2(puntaje, nombre):
    if puntaje> 65:
        print("apenas pasaste", nombre)
    else:
        print("no hule ya", nombre)
    if puntaje== 65:
        print("igualito pero no", nombre)
notas2(66, "gabriel")
notas2(64, "pepito")
notas2(67, " sime")
notas2(65, "carlos")

#----------------------------------------------
a= 11
if a > 5 and a < 10: # and su fincion es "y"
    print(" a no es mayor a 5 y menor que 10")
else:
    print(" a no eta en el rango, de alguna de las condiciones no se cumplieron")

if a > 5 or a < 10: # or da la posivilidad de que se cumpla 1 o ambas de las condiciones
    print("a es mayor que 5 y menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")


False
True
print(5>3)
print(5==3)

#elif # si no, si
# else en caso de que no cumola nunguna de las funciones o poaramwetros
edad = 0

if edad> 18:
    print("deberia estar en la universidad")
elif edad > 13:
    print("deberia estar en la secundaria")
elif edad > 6:
    print("deberia estar en primaria")
elif edad > 1:
    print(" deberia estar en la casa")
else:
    print(" deberia estar en la pansa")



# ejee. crear funcion puntaje que reciba como parametro una nota 
# del 1 al 100 e imprimir que nota sacaste
# nota < 60 -----> 1
# nota entre 60 y 70 -----> 2
# nota entre 71 y 75 -----> 3
# nota entre 76 y 85 -----> 4
# nota mayor a 85 -----> 5


nota= 58
def notas(puntaje):
    if puntaje< 60:
        print("1 aplasado")
        return 1
    elif puntaje> 60 and puntaje< 70:
        print("2 apenitas")
        return 2
    elif puntaje> 71 and puntaje< 75:
        print(" 3 omarcha")
        return 3
    elif puntaje< 76 and puntaje< 85:
        print(" 4 super bien")
        return 4
    elif puntaje>85:
        print("5 que purete")
        return 5
    
notas(51)
notas(89)    
notas(73)   
notas(66)    
# ejer. pedir al usuario ingresar 3 numeros y multiplicar entre si, imprimir el resultado


numero1 = int(input("este por"))
numero2 = int(input(" por"))
numero3 = int(input(" y este"))
print("te sale: ", numero1 * numero2 * numero3)


# ejer2. pedir al usuario un nro del 1 al 100 y llamar a la funcion que retornaba la nota que creamos hace un rato 
# utilizando el valor ingresado por el usuario

nombre = int(input("ha upei podes ingresar la nota que saco del 1 al 100: "))
notas(nombre)










