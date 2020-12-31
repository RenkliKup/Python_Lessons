def pass_kontrol(pwd):
    import re
    if len(pwd)<8:
         raise Exception("Parola 8 den küçük olamaz")
    elif not re.search("[a-z]",pwd):
         raise Exception("küçük harf olmalı")
    elif not re.search("[A-Z]",pwd):
         raise Exception("buyuk harf olmalı")
    elif not re.search("[0-9]",pwd):
         raise Exception("rakam olmalı")
    elif not re.search("[_@$]",pwd):
        raise Exception("Alpha numeric sayı olmalıdır")
    elif re.search("\s",pwd):
        raise Exception("boşluk olmamalı")
    else:
        print("Başarılı bir şekilde oluşturuldu")
password="1234567aB_"
try:
    pass_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("basarılı")


    
