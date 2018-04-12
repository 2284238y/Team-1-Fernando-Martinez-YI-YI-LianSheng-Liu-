{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh17520\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def based_on_photo_transistor():\
    global up,down\
    print("Photo Transistor started...")\
    stable = 0\
    count=0\
    while(True):\
        inp = GPIO.input(PIN)==GPIO.LOW\
        if(not inp):\
            stable+=1\
        else:\
            stable-=1\
    \
        if(stable>10 and not up):\
            go_up()\
            up = True\
            down = False\
            stable=0\
            count=0\
        elif(stable<-10 and not down):\
            go_down()\
            down = True\
            up = False\
            stable=0\
            count\
        else:\
            if(count>30):\
                stable = 0\
                count = 0\
    \
        count+=1\
        #print(stable,count)\
        time.sleep(2)        \
\
}