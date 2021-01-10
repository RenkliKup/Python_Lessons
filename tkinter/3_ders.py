from tkinter import *
pencere=Tk()
pencere.geometry("200x200")
pencere.title("uygulama1")
var=0;
def dialog(alfa):
     global var
     var+=1
     print("Merhaba:",var)
     Button1.config(text=f"Merhaba {alfa} {var}" )




Button1=Button(pencere,text="Merhaba",command=lambda:dialog("baris"))
Button1.grid(column=0,row=0)
pencere.mainloop()
