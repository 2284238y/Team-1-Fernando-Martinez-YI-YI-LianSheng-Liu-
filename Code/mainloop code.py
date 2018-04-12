import RPi.GPIO as GPIO
import time
import datetime
import sys
import tkinter as tk
import threading

PIN = 7
PWM_PIN = 3

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN,GPIO.IN)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setwarnings(False)

up = False
down = False

pwm = GPIO.PWM(PWM_PIN,50)
pwm.start(14)

def go_up():
    global up,down,pwm
    if up:
        print("Curtain is already up")
        return
    up = True
    down = False
    pwm.ChangeDutyCycle(14)
    print("Curtains should go up")

def go_down():
    global up,down,pwm
    if down:
        print("Curtain is already down")
        return
    up = False
    down = True
    pwm.ChangeDutyCycle(2)
    print("Curtains should go down")



def main():
    t1 = threading.Thread(target=based_on_photo_transistor, args=[])
    t2 = threading.Thread(target=based_on_interface, args=[])
    t3 = threading.Thread(target=based_on_time, args=[])
    t1.start()
    t2.start()
    t3.start()


if __name__== "__main__":
   main() 

