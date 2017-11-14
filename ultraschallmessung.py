import RPi.GPIO as GPIO
import time

#GPIO PIN's zuweisen

GPIO_TRIGGER =                    		#pin 24 vorwärts fahren rechts
GPIO_ECHO =                     		#pin 18 aktivieren und Geschwindigkeit rechts

def distanz ():
	#10us Puls erzeugen
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(10e-3)
	GPIO.output(GPIO_TRIGGER, False)

	#warten auf LOW (Start der Messung)
	while GPIO.input(GPIO_ECHO) == 0:
		StartZeit = time.time()

	#warten auf HIGH (Echo empfangen)
	while GPIO.input(GPIO_ECHO) == 1:
		StopZeit = time.time()

	#Entfernungsberechnung
	Techo = StopZeit - StartZeit
	distanz = (Techo * 33e3) / 2
	return distanz

#Eingang / Ausgang definieren
GPIO.Setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
	while True:
		abstand = distanz()
		print ("Entfernung = %.1f cm" % abstand)
		time.sleep(1)

except KeyboardInterrupt:
	print("Messung vom User gestoppt")
	GPIO.cleanup()
