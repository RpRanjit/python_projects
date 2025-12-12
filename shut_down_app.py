from tkinter import *
import os

shut_down = Tk()

shut_down.title("ShutDown App")
shut_down.geometry("500x500")
shut_down.config(bg="blue")



# functions

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system ("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

restart_btn = Button(shut_down, text="Restart", font=("Time New Roman", 20, "bold"), 
                     relief=RAISED, cursor="plus", command= restart)
restart_btn.place(x = 150, y = 90, height = 60, width = 200)

restart_time_btn = Button(shut_down, text="Restart Time", font=("Time New Roman", 20, "bold"), 
                          relief=RAISED, cursor="plus", command= restart_time)
restart_time_btn.place(x = 125, y = 180, height = 60, width = 250)

restart_time_btn = Button(shut_down, text="Log-out", font=("Time New Roman", 20, "bold"), 
                          relief=RAISED, cursor="plus", command= log_out)
restart_time_btn.place(x = 150, y = 270, height = 60, width = 200)

restart_time_btn = Button(shut_down, text="ShutDown", font=("Time New Roman", 20, "bold"), 
                          relief=RAISED, cursor="plus", command= shutdown)
restart_time_btn.place(x = 137, y = 360, height = 60, width = 225)


shut_down.mainloop()