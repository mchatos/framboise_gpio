#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
blink_one_two.py
Leds clignotantes une par une par deux par une sur GPIO via des résistances de 330 Ohms
logiciel            : python 3.4.2
cible               : raspberry Pi
date de création    : 20/10/2018
date de mise à jour : 20/10/2018
version             : 1.0
auteur              : Patou
référence           : 
"""

#-------------------------------------------------------------------------------
# Bibliothèques
import RPi.GPIO as GPIO                 #bibliothèque RPi.GPIO
import time                             #bibliothèque time
import sys

#-------------------------------------------------------------------------------
# Fonctions
def button_callback(channel):
    print("Button was pushed!")
    print("The end is coming !!")
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()
    time.sleep(0.1)
    sys.exit(0)
    
#-------------------------------------------------------------------------------
# VAR et GPIO
button=2
leds=[23,24,18,15,14]									#Declaration array leds
nbLeds=len(leds)

GPIO.setwarnings(False)                 				#désactive le mode warning
GPIO.setmode(GPIO.BCM)                  				#utilisation des numéros de ports du processeur
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#Declaration push button
GPIO.setup(leds, GPIO.OUT)                				#mise en sortie des ports GPIO de l'array leds (broche 16 du connecteur)
GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback)

#-------------------------------------------------------------------------------
# main
if __name__ == '__main__':

		print("Début du clignotements des LEDs")
		while True :                        				#boucle infinie
			for i in range(len(leds)) :

				if leds[i] == leds[-nbLeds] :
					GPIO.output(leds[i+4], GPIO.LOW)
					
				GPIO.output(leds[i-2], GPIO.LOW)
				GPIO.output(leds[i], GPIO.HIGH)
				time.sleep(1)
				
				if leds[i] == leds[nbLeds-1] :
					GPIO.output(leds[i-1], GPIO.LOW)
					time.sleep(1)

#-------------------------------------------------------------------------------
