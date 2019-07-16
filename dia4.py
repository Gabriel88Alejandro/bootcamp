import rodi #para importar los comandos a utilizar 
import time

robot = rodi.RoDI() # instanciamos y creamos el objeto robot
'''
robot.move_forward() #mueve hacia adelante
time.sleep(1)         # queda haciendo lo anterior por 1 segundo     
robot.move_left()     # hace un giro a la izquierda
time.sleep(1)         # queda haciendo el movimiento a la izquierda por 1 segundo
robot.move_right()    # GIRO A LA DERECHA




#ejer1. hacer un cuadrado
robot.move_forward()
time.sleep(1)
robot.move_stop()
time.sleep(0.5)
robot.move_right
time.sleep(0.5)time.sleep(1)
robot.move_stop()
time.sleep(0.5)
robot.move_right
time.sleep(0.5)time.sleep(1)
robot.move_stop()
time.sleep(0.5)
robot.move_right
time.sleep(0.5)time.sleep(1)
robot.move_stop()
time.sleep(0.5)
robot.move_right
time.sleep(0.5)
robot.move_stop()

# con for

for movimiento in range(4):
    robot.move_forward()
    time.sleep(2)
    robot.move_left()
    time.sleep(0.5)
    robot.move_stop()

# con while


contador = 0
while contador <== 3:
    contador = contador + 1
    robot.move_forward()
    time.sleep(2)
    robot.move_stop()
    robot.move_left()
    time.sleep(0.5)
    robot.move_stop()
    '''



    ###### -------------- ####
  # sensores de distacia

'''
variable = 3

while True:
    print(robot.see(), "cm")   # para que repita de forma infinita mientras el objeto se acerca usando un bucle infinito
'''
try:                   #intentar esto
    while True:
        print(robot.see(), "centimetros") # imprime la distacia
        robot.move_forward()              # movemos el robot hacia adelante
except KeyboardInterrupt:                 # exepto cuando hay una interrupcion por teclado
    print("finalizado")                   # al apretar ctrlc  para el robot
    robot.move_stop()



    # ejr. utilizando while tru( bucle infinito), hacer que RoDI avanse si no encuentra un obstaculo en frente

try:
    while True: 
        cm= robot.see()
        print(cm)
        if cm >= 10:
            robot.move_forward()
        else:
            robot.move_stop()
            robot.move_right()
            time.sleep(0.5)              
except KeyboardInterrupt:                 
    print("finalizado")                   
    robot.move_stop()


# ejer2. hacer que el robot siga un objeto 


try:
    while True: 
        print(robot.see(), "cem")
        cm = robot.see()
        if cm >= 55:
            robot.move(10,10)
            robot.move_right()
            robot.pixel(0, 100, 0)
            robot.move_left()
        elif cm <= 25:
            robot.move(100,100)
except KeyboardInterrupt:                 
    print("finalizado")                   
    robot.move_stop()

    while True:
        print(robot.light()) # sensor de luz RoDI, muestra la cantidad de luz que recibe del ambiente
        time.sleep(0.5)
        robot.sing(800, 1000) # sensor de sonido

while True:
    linea= robot.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    time.sleep(0.10) 