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

def based_on_time():
    global up,down
    print("Time started...")
    now = datetime.datetime.now()
    while(True):
        now = datetime.datetime.now()
        if(now.hour=="5" or now.hour==5 and not up): 
            go_up()
            up = True
            down = False
        elif(now.hour=="19" or now.hour==19 and not down):
            go_down()
            up = False
            down = True
        time.sleep(1200)



def based_on_interface():
    print("Interface started...")
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    quit_button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
    quit_button.pack(side=tk.LEFT)
    quit_button.config( height = 10, width = 10 )
    up_button = tk.Button(frame,
                   text="Up",
                   command=go_up)
    up_button.pack(side=tk.LEFT)
    up_button.config( height = 10, width = 10 )
    down_button = tk.Button(frame,
                   text="Down",
                   command=go_down)
    down_button.pack(side=tk.LEFT)
    down_button.config( height = 10, width = 10 )
    root.mainloop()

def based_on_photo_transistor():
    global up,down
    print("Photo Transistor started...")
    stable = 0
    count=0
    while(True):
        inp = GPIO.input(PIN)==GPIO.LOW
        if(not inp):
            stable+=1
        else:
            stable-=1
    
        if(stable>10 and not up):
            go_up()
            up = True
            down = False
            stable=0
            count=0
        elif(stable<-10 and not down):
            go_down()
            down = True
            up = False
            stable=0
            count
        else:
            if(count>30):
                stable = 0
                count = 0
    
        count+=1
        #print(stable,count)
        time.sleep(2)        

def main():
    t1 = threading.Thread(target=based_on_photo_transistor, args=[])
    t2 = threading.Thread(target=based_on_interface, args=[])
    t3 = threading.Thread(target=based_on_time, args=[])
    t1.start()
    t2.start()
    t3.start()


if __name__== "__main__":
   main() 

