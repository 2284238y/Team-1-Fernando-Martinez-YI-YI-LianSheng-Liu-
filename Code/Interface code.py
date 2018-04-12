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

