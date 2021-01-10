from tkinter import *
asilisim="baris"
asilsifre="1234"
pencere=Tk()
pencere.geometry("500x250")
def girisyapma():
    isim=isimgiris.get()
    sifre=sifregiris.get()
    if isim==asilisim and asilsifre==sifre:
        label2.config(text="Giriş Başarılı",bg="green")
    else:
        label2.config(text="Ad veya şifre hatalı!!")

label1=Label(pencere,text="Adınız")
label1.grid(column=0,row=0)
isimgiris=Entry(pencere,width="8")
isimgiris.grid(column=1,row=0)
label2=Label(pencere,text="Şifre")
label2.grid(column=0,row=1)
sifregiris=Entry(pencere,width="8")
sifregiris.grid(column=1,row=1)
giris=Button(pencere,text="Giriş",command=girisyapma)
giris.grid(column=0,row=2)
label2=Label(pencere,text="")
label2.grid(column=1,row=2)
pencere.mainloop()
