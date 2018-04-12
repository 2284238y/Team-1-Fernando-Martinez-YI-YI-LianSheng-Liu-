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



