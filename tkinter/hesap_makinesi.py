from tkinter import *
pencere=Tk()
pencere.geometry("500x500")
pencere.title("Hesap Makinesi")
kasa=[]

def guncelle(deger):
    var=label1.get()+deger
    label1.delete(0,END)
    label1.insert(0,var)
    return var

def islem(deger1):
    icerik=label1.get() 
    if len(kasa)==0:
        kasa.append(guncelle(""))
        kasa.append(deger1)
        label1.delete(0,END)
    elif icerik=="" and len(kasa)==2 and (deger1=="+" or deger1=="-",deger1=="*",deger1=="/") :
        kasa[1]=deger1
        label1.delete(0,END)
    elif icerik!="" and len(kasa)==2 and (deger1=="+" or deger1=="-",deger1=="*",deger1=="/"):
        print(kasa)
        if kasa[1]=="+":
            kasa[0]=int(kasa[0])+int(icerik)
        elif kasa[1]=="-":
            kasa[0]=int(kasa[0])-int(icerik)
        elif kasa[1]=="*":
            kasa[0]=int(kasa[0])*int(icerik)
        elif kasa[1]=="/":
            if(icerik=="0"):
                raise Exception("0 a bölme hatası")
            else:
                kasa[0]=int(kasa[0])/int(icerik)
    
        label1.delete(0,END)
        label1.insert(0,kasa[0])


        
            
label1=Entry(pencere)
label1.insert(0,"")
label1.grid(columnspan=6,row=0)
Button_001=Button(pencere,text="1",command=lambda:guncelle(str(1)))
Button_001.grid(column=0,row=1,pady=10,padx=5)
Button_002=Button(pencere,text="2",command=lambda:guncelle(str(2)))
Button_002.grid(column=1,row=1,pady=10,padx=5)
Button_003=Button(pencere,text="3",command=lambda:guncelle(str(3)))
Button_003.grid(column=2,row=1,pady=10,padx=5)
Button_004=Button(pencere,text="4",command=lambda:guncelle(str(4)))
Button_004.grid(column=3,row=1,pady=10,padx=5)
Button_005=Button(pencere,text="5",command=lambda:guncelle(str(5)))
Button_005.grid(column=4,row=1,pady=10,padx=5)
Button_006=Button(pencere,text="6",command=lambda:guncelle(str(6)))
Button_006.grid(column=0,row=2,pady=10,padx=5)
Button_007=Button(pencere,text="7",command=lambda:guncelle(str(7)))
Button_007.grid(column=1,row=2,pady=10,padx=5)
Button_008=Button(pencere,text="8",command=lambda:guncelle(str(8)))
Button_008.grid(column=2,row=2,pady=10,padx=5)
Button_009=Button(pencere,text="9",command=lambda:guncelle(str(9)))
Button_009.grid(column=3,row=2,pady=10,padx=5)
Button_000=Button(pencere,text="0",command=lambda:guncelle(str(0)))
Button_000.grid(column=4,row=2,pady=10,padx=5)
Button_arti=Button(pencere,text="+",command=lambda: islem("+"))
Button_arti.grid(column=0,row=3,pady=10,padx=5)
Button_eksi=Button(pencere,text="-",command=lambda: islem("-"))
Button_eksi.grid(column=1,row=3,pady=10,padx=5)
Button_carp=Button(pencere,text="*",command=lambda: islem("*"))
Button_carp.grid(column=2,row=3,pady=10,padx=5)
Button_bol=Button(pencere,text="/",command=lambda: islem("/"))
Button_bol.grid(column=3,row=3,pady=10,padx=5)
Button_esittir=Button(pencere,text="=",command=lambda:islem("="))
Button_esittir.grid(row=4,column=0,rowspan=6)


pencere.mainloop()

