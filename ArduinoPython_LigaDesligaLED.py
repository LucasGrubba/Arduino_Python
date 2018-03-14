import serial # biblioteca necessaria para comunicaçao serial com o Arduino
import time

arduino = serial.Serial('COM4',9600) # configura a porta serial

def ligaDesliga():
    comando = input("Digite uma opção: (On | Off | Sair) ")
    
    if comando == "On":
        print("LED: On")
        time.sleep(1)
        arduino.write('H'.encode())
        ligaDesliga()
            
    elif comando == "Off":
        print("LED: Off")
        time.sleep(1)
        arduino.write('L'.encode())
        ligaDesliga()
            
    elif comando == "Sair":
        print("Fim")
        time.sleep(1)
        arduino.close()

    else:
        print("Opção inválida...")
        ligaDesliga()

time.sleep(2) # espera a inicializaçao

ligaDesliga()
