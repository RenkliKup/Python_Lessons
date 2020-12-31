
while True:

    try:
        x=int(input("x:"))
        y=int(input("y:"))
        sonuc=x/y
        print(sonuc)
    except Exception as e:
        print("hatalı sayı girişi Hata Kodu:",e)
    else:
        break
