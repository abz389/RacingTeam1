import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.output(23, 1)
GPIO.output(24, 1)

GPIO.setup(21, GPIO.OUT)	#Ausgang Motoren rechts
GPIO.setup(18, GPIO.OUT)	#Ausgang Motoren links


d = GPIO.PWM(21, 2) 		#Kanal 18, 2Hz, green
d.start(50)			#Tastverhältnis 50%

s = GPIO.PWM(18, 2)		 #Kanal 20, 2Hz, yellow
s.start(50) 			#Tastverhältnis 50%


input('Press return to stop:')
d.stop()
s.stop()

GPIO.cleanup()
