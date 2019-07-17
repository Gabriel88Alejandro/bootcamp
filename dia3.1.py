# ##################### bucle "while" = miemtras  #########################

# x= 0
# while x != 5: # mientras x sea distindo a 5 va  a hacer lo siguinte 
#     print("esto es un bucle while, se ejecuta mientras x sea distinto a 5")
#     x = int(input("ingresa un numero: ")) # reingresamos un valor para x
#     print("el valor de x ahora es ")
# print("termino!!!")

# # contador inverso 
# contador = 10
# while contador < 0:
#     print("sigo en el bucle while")
#     contador = contador - 1
#     print("te quedan", contador, "oportunidades")
# print("termino")
     

# # contador  
# contador = 0
# while contador < 10:
#     print("sigo en el bucle while")
#     contador = contador + 1
#     print("se repitio", contador, "veces")

# usando while pedir al usuario 5 ingredientes par ahacer una pizza 
# y agregar a una lista, al final imprimir la lista

lista_ingredientes = []
ingrediente = 1
while ingrediente <= 5:
    ingrediente = ingrediente + 1
    #lista_ingredientes.append(input("pone tus ingredientes:"))
print("esto tiene tu pizza", lista_ingredientes)

# ejer. crear un juego de adivinar el nro y darle pistas al usuario si e nro que ingreso es mayor o menor
# al nro a adividar
# pista elif

numero_secreto= 3
adivino = False
while adivino == False:
    apuesta = input("adiviva adivinador, cual es el nro que quiero yo: ")
    if int(apuesta) == numero_secreto:
        print("bien ahi!!")
        adivino= True
    elif int(apuesta) <numero_secreto:
        print( "es un nro mayor, segui nomas")
    elif int(apuesta) >numero_secreto: 
        print(" es un numero menor, metele nomas")

# ejer2. buscar como generar numero aleatoria para numero_secreto




