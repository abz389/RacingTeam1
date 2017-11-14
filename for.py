import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DIRA = 24                   		#pin 24 vorwärts fahren rechts
PIN_ENA = 18                    		#pin 18 aktivieren und Geschwindigkeit rechts
PIN_DIRB = 23                   		#pin 23 vorwärts fahren links
PIN_ENB = 17                    		#pin 17 aktivieren und Geschwindigkeit links

input('press retrn to start')

GPIO.setup(PIN_DIRA, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_DIRB, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)
MotorA = GPIO.PWM(PIN_ENA, 50.0)  	#rechts ansteuern mit 50Hz
MotorB = GPIO.PWM(PIN_ENB, 50.0)   	#links ansteuern mit 50HZ
MotorA.start(75)                		#rechts tastverhaeltniss 70%
MotorB.start(75)                   		#links tastverhaeltniss 50%


GPIO.output(PIN_DIRA, 1)           #rechts aktivieren
GPIO.output(PIN_DIRB, 1)           #links aktivieren

    
    
input('Press return to stop:')

    
    
MotorA.stop()
MotorB.stop()

GPIO.cleanup()