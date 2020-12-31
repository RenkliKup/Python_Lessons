import re

liste=["10","2","5a","10b","abc","10","50"]

for x in liste:
    try:
        int(x)
    except:
        continue
    '''
    if re.search("[a-b]",x):
       continue
    else:
         print(x)
    '''
    '''
while True:
    sayi=input("sayı: ")
    if sayi=="q":
        break
    else:
        try:
            int(sayi)
        except ValueError:
            print("integer olmayan sayı girişi")
            break
        else:
            continue

'''
'''
def new_func(turkce_karakter, parola):
    for i in parola:
        if(i in turkce_karakter):
            raise Exception("Türkçe Karakter Var")
        else:
            continue
while True:
    try:
        turkce_karakter="şçğüöıİ"

        parola=input("Parola:")
        new_func(turkce_karakter, parola)
    except Exception as ex:
        print(ex)
        continue
    else:
        print("Parola oluşturuldu")
        break

'''
'''
def factoriyel(x):
    if x<0:
        raise Exception("Girilen Değer 0 da küçük")
    else:
        result=1
        for i in range(1,x+1):
            result*=i
    return result
while True:
    try:
        deger=int(input("Deger:"))
        print(factoriyel(deger))
        
    except Exception as ex:
        print(ex)
        continue
    else:
        break
'''