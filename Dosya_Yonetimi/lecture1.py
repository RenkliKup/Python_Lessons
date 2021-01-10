'''
open()
"r" "okuma"
"x"  "oluşturma"
"a"  "ekleme"
"w"  "üstüne yazmaz"
'''
'''
file=open("ornek.txt","w",encoding="utf-8")
file.write("Hello, World 2")
file.close()
'''
'''
file=open("ornek.txt","a",encoding="utf-8")
file.write("Merhaba Ben Barış\n")
file.close()
'''
file=open("ornek1.txt","x",encoding="utf-8")
file.write("\nmerhaba")
file.close()