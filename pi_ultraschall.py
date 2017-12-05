#In Anlehnung an https://tutorials−raspberrypi.de/
#entfernung−messen−mit−ultraschallsensor−hc−sr04/
import RPi.GPIO as GPIO
import time

#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24

def distanz():
    #10us Pulserzeugen
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(10e-3)
    GPIO.output(GPIO_TRIGGER, False)

    #Warten auf LOW (Start der Messung)
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time ()

    #Warten auf HIGH (Echo empfangen)
    while GPIO.input (GPIO_ECHO) == 1:
        StopZeit = time.time()
    #Entfernungsberechnung
    Techo = StopZeit - StartZeit
    distanz =(Techo*33e3)/2
#    print('Echozeit: %5.2fms ==> %.2fcm'%(Techo*1e3, distanz))
    return distanz

28 #Eingang / Ausgang definieren
GPIO.setmode (GPIO.BCM)
GPIO.setup (GPIO_TRIGGER, GPIO.OUT)
GPIO.setup (GPIO_ECHO, GPIO.IN)

soll = 25
P = 1.0
I = 1.0
regler_I = 0
T0 = 0
ersterdurchlauf = True
try:
    while True:
        T1 = T0
        T0 = time.time()
        dt = T0-T1

        if not ersterdurchlauf:
            abstand = distanz()
            error = soll - abstand
            regler_I += I*error*dt
            regler_P = P*error
            if regler_I < -100:
                regler_I = -100
            if regler_I > 100:
                regler_I = 100
            regler = regler_I + regler_P
            print(regler, abstand, error, dt)
        #print("Gemessene Entfernung = %.1f cm" % abstand)
        time.sleep(.1)
        ersterdurchlauf = False

except KeyboardInterrupt :
    print ("Messung vom User gestoppt")
    GPIO.cleanup()
