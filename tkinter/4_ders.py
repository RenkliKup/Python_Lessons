from tkinter import *
from tkinter import messagebox
from time import sleep

pencere=Tk()
uygulama=Frame(pencere)
uygulama.grid()
pencere.geometry("500x500")
def goster():
    
    var=messagebox.showinfo("Uyarı","Python Programlama")
    sleep(2)
    var2=messagebox.askyesnocancel("Uyarı","Python Programlama")
    if var2==True:
        return goster()

Button1=Button(uygulama,text="Göster",command=goster)
Button1.grid(padx=250,pady=250)
pencere.mainloop()