mkdir			-	Verzeichnis erstellen
cat[Dateiname]		-	Dateiinhalt anzeigen
touch			-	leere Datei erstellen ohne Inhalt
rm [Dateiname]	-	Datei löschen, Datei remove
ls			-	Anzeigen der Dateien
cd ..			-	in der Dateistruktur zurück
rm -rf [Dateiname]	-	löschen der Datei (komplett)
cd [Dateiname]		-	auf Datei zugreifen

https://heinrich.mt.haw-hamburg.de		Jupiter-Notebook

auf raspi einloggen : ip-adresse:8000

git bash – starten
in den Ordner haw/it-systeme/git gehen mit cd pro ordner
1.	Dokument erstellen
2.	

PIN-Belegung Motormodul zu Raspi
PIN 17 = enable + geschwindigkeit links
PIN 18 = enable + geschwindigkeit rechts
PIN 25 = rückwärts rechts
PIN 12 = rückwärts links
PIN 24 = vorwärts rechts
PIN 23 = vorwärts links 





Beispiel 3 LED’s blinken
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)	#Ausgang 21
GPIO.setup(18, GPIO.OUT)	#Ausgang 18
GPIO.setup(20, GPIO.OUT)	#Ausgang 20

d = GPIO.PWM(18, 2) 		#Kanal 18, 5Hz, green
d.start(50)			#Tastverhältnis 50%

s = GPIO.PWM(20, 1)		 #Kanal 20, 1Hz, yellow
s.start(50) 			#Tastverhältnis 90%

a = GPIO.PWM(21, 0.5) 		#Kanal 21, 0.5Hz, red
a.start(50) 			#Tastverhältnis 10%

input('Press return to stop:')
d.stop()
s.stop()
a.stop()

GPIO.cleanup()
 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)		 #    Ausgang

p = GPIO.PWM(20, 5)			 #Kanal 18, 0.5Hz	
p.start(4)				 #Tastverhältnis 70%
input('Press return to stop:')
p.stop()



GPIO.cleanup()
 
Motor Test “car1.py”
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DIRA = 24   				# pin vorwärts fahren links
PIN_ENA = 18    				# pin aktivieren und geschindigkeit links
PIN_DIRB = 23   				# pin vorwärts fahren rechts
PIN_ENB = 19   					# pin aktivieren und geschindigkeit rechts

input('press return to start') 			#return drücke zum starten

GPIO.setup(PIN_DIRA, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_DIRB, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)
MotorA = GPIO.PWM(PIN_ENA, 70.0)
MotorB = GPIO.PWM(PIN_ENB, 50.0)

GPIO.output(PIN_DIRA, 1)
GPIO.output(PIN_DIRB, 1)

for i in range(0, 11):				#zähler bis 10 und dann stop
    d = 1
    GPIO.output(PIN_DIRA, d)
    GPIO.output(PIN_DIRB, d)

    MotorA.start(i*10)
    MotorB.start(i*10)
    print(i)
    time.sleep(0.3)

    
    
MotorA.stop()
MotorB.stop()

GPIO.cleanup()












“car2.py” – gerade ausfahren mit 50Hz

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DIRA = 24                   		#pin 24 vorwärts fahren links
PIN_ENA = 18                    		#pin 18 aktivieren und Geschwindigkeit links
PIN_DIRB = 23                   		#pin 23 vorwärts fahren rechts
PIN_ENB = 17                    		#pin 17 aktivieren und Geschwindigkeit rechts

input('press retrn to start')

GPIO.setup(PIN_DIRA, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_DIRB, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)
MotorA = GPIO.PWM(PIN_ENA, 50.0)  	#links ansteuern mit 50Hz
MotorB = GPIO.PWM(PIN_ENB, 50.0)   	#rechts ansteuern mit 50HZ
MotorA.start(70)                		#links tastverhaeltniss 70%
MotorB.start(50)                   		#rechts tastverhaeltniss 50%


GPIO.output(PIN_DIRA, 1)           #links aktivieren
GPIO.output(PIN_DIRB, 1)           #rechts aktivieren

    
    
input('Press return to stop:')

    
    
MotorA.stop()
MotorB.stop()

GPIO.cleanup()
