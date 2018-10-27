#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
blink_one_by_one.py
Leds clignotantes une par une sur GPIO via des résistances de 330 Ohms
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
button=27
#leds=[21,20,16,1,7,8,25,24]								#Declaration array leds
leds=[26,16,6,5,25,24,23,22]	

GPIO.setwarnings(False)                 				#désactive le mode warning
GPIO.setmode(GPIO.BCM)                  				#utilisation des numéros de ports du processeur
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#Declaration push button
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)			#mise en sortie des ports GPIO de l'array leds (broche 16 du connecteur)
GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback)

#-------------------------------------------------------------------------------
# main
if __name__ == '__main__':

		print("Début du clignotements des LEDs")
		while True :                        				#boucle infinie
			for i in range(len(leds)) :
				print ("led : ", leds[i],"led -1 : ", leds[i-1])
				GPIO.output(leds[i], GPIO.HIGH)
				GPIO.output(leds[i-1], GPIO.LOW)
				time.sleep(0.3)

#-------------------------------------------------------------------------------
