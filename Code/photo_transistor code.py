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