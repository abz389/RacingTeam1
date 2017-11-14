import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DIRA = 24                   		#pin 25 vorwärts fahren rechts
PIN_ENA = 18                    		#pin 18 aktivieren und Geschwindigkeit rechts
PIN_DIRB = 23                   		#pin 12 vorwärts fahren links
PIN_ENB = 17                    		#pin 17 aktivieren und Geschwindigkeit links

input('press retrn to start')

GPIO.setup(PIN_DIRA, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_DIRB, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)
MotorA = GPIO.PWM(PIN_ENA, 50.0)  	
MotorB = GPIO.PWM(PIN_ENB, 50.0)   	
MotorA.start(75)                		
MotorB.start(2)                   		

GPIO.output(PIN_DIRA, 1)           #rechts aktivieren
GPIO.output(PIN_DIRB, 1)           #links aktivieren
 
input('Press return to stop:')

    
MotorA.stop()
MotorB.stop()

GPIO.cleanup()
