website="http://www.sadikturan.com"
course="Python Kursu: Baştan sona python programlama rehberiniz (40 saat)"

#1 course karakter dizisinde kaç karakter bulunmaktadır.
print(len(course))
#2 website içinden www karakterlerini alın
print(website[7:10])
#3 webside içinden com karakterlerini alın
print(website[len(website)-3:len(website)])
#4 course içinden ilk 15 ve son 15 karakterlerini alın
print("ilk 15 karakter= " +course[:15]+" , "+"son 15 karakter= "+course[len(course)-16:])
result="12345"*5
print(result);
print(result[::5])
print(course[::-1])#ters olarak yazar

name,surname,age,job="Bora","Yılmaz",32,"Mühendis"

result="Benim adım "+name+" "+surname+", Yaşım "+str(age)+" ve mesleğim "+job
result="Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}".format(name=name,surname=surname,age=age,job=job)
result=f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}"
s="Hello world"
s=s[0:6]+"W"+s[-4:]
s=s.replace('W',"w")
print(s)

print(result)