import RPi.GPIO as GPIO
import time


					#GPIO PIN's zuweisen
GPIO.setmode(GPIO.BCM)



GPIO_TRIGGERright = 20
GPIO_ECHOright = 21


def distanz(distanzright):
					#10us Puls erzeugen
	GPIO.output(GPIO_TRIGGERright, True)
	time.sleep(10e-3)
	GPIO.output(GPIO_TRIGGERright, False)

					#warten auf LOW (Start der Messung)
	while GPIO.input(GPIO_ECHOright) == 0:
		StartZeit = time.time()

					#warten auf HIGH (Echo empfangen)
	while GPIO.input(GPIO_ECHOright) == 1:
		StopZeit = time.time()

					#Entfernungsberechnung
	Techo = StopZeit - StartZeit
	distanzright = (Techo * 33e3) / 2
	return distanzright

GPIO.setup(GPIO_TRIGGERright, GPIO.OUT)
GPIO.setup(GPIO_ECHOright, GPIO.IN)

try:
      
	while True:
		abstandright = distanzright()
        
		print (abstandright)
        
		time.sleep(1)
             
except KeyboardInterrupt:
    
	print("Messung vom User gestoppt")
      
    
GPIO.cleanup()
