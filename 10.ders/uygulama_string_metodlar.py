website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1
string=" Hello World "
string=string.strip()
string=string.lstrip()#soldakileri silmek için
string=string.rstrip()#sagdakileri silmek için
print(string)
#2
#string1=website.replace("http://www.","").replace(".com","")
string1=website.strip("htp:/w.com")
print(string1)
#3
string2=course.lower()
print(string2)
#4
string3=website.count("a")
print(string3)
#5
string4=website.startswith("www")
string5=website.endswith(".com")
print("www= "+str(string4)+"\n.com= "+str(string5))
#6
string6=website.find(".com")
print(string6)
#7
string7=course.isalpha()#isdigit()
print(string7)
#8
string8="content".center(50,"*")
print(string8)
#11
string9=course.split(" ")
print(string9)