from tkinter import *
import speedtest


def speedCheck():
    speed = speedtest.Speedtest()
    speed.get_servers()
    # Here we get the data in bit/s but we have to get in Mbps so divided bt 10**6
    download = str(round(speed.download()/(10**6),3))+ " Mbps"
    upload = str(round(speed.upload()/(10**6),3))+ " Mbps"
    lab_download.config(text=download)
    lab_upload.config(text=upload)


sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("550x500")
sp.config(bg = "blue")

lab = Label(sp, text = " Internet Speed Test ", font=("Times New Roman", 30, "bold"), bg= "blue", fg= "red")
lab.place(x = 90, y= 40)

lab = Label(sp, text = " Download Speed ", font=("Times New Roman", 20, "bold"), bg= "blue", fg= "black")
lab.place(x = 50, y= 160)

lab_download = Label(sp, text = "00", font=("Times New Roman", 20, "bold"), bg= "blue", fg= "white")
lab_download.place(x = 100, y= 210)

lab = Label(sp, text = " Upload Speed ", font=("Times New Roman", 20, "bold"), bg= "blue", fg= "black")
lab.place(x = 300, y= 160)

lab_upload = Label(sp, text = "00", font=("Times New Roman", 20, "bold"), bg= "blue", fg= "white")
lab_upload.place(x = 350, y= 210)

button = Button(sp, text="Check Speed", font= ("Time new Roman", 25 , "bold"), bg="black", fg="white", relief= RAISED, command=speedCheck)
button.place(x= 150, y = 310)


sp.mainloop()