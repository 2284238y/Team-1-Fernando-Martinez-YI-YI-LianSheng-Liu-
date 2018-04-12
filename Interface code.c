{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15140\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def based_on_interface():\
    print("Interface started...")\
    root = tk.Tk()\
    frame = tk.Frame(root)\
    frame.pack()\
    quit_button = tk.Button(frame, \
                   text="QUIT", \
                   fg="red",\
                   command=quit)\
    quit_button.pack(side=tk.LEFT)\
    quit_button.config( height = 10, width = 10 )\
    up_button = tk.Button(frame,\
                   text="Up",\
                   command=go_up)\
    up_button.pack(side=tk.LEFT)\
    up_button.config( height = 10, width = 10 )\
    down_button = tk.Button(frame,\
                   text="Down",\
                   command=go_down)\
    down_button.pack(side=tk.LEFT)\
    down_button.config( height = 10, width = 10 )\
    root.mainloop()\
}