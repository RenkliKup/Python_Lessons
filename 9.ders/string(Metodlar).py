message=" Hello there. my name is Barış karakulak"
#message=message.upper()#bütün karakterleri büyük yapar
#message=message.lower()#bütün karakterleri küçük yapar
#message=message.title()#her kelimenin baş harfi büyük harfe çevrilir
#message=message.capitalize()#ilk karakter büyük olur diğerleri küçük
#message=message.strip()#baştaki boşlukları siliyor
#message=message.split()#her boşlukta bir dizi elemanı oluyor
#message=message.split('.')#noktalardan itibaren diziye yerleştirir
#message=message.split()
#message=' '.join(message)#ayrılmış harfleri boşluk ile birleştirir 
#index=message.find('Barış')#string de kelime bulma bulduğu kelimeninin ilk haarfinin index numarasını döndürür
#isFound=message.startswith(" ")#string hangi harfle başlıyorsa true döndürür 
#isFound=message.endswith('k')#string hangi harfle bitiyorsa
#message=message.replace('H','a')#string degerdeki H karakterini a ile değiştirdi
#message=message.replace("ö","o").replace("ç","c").replace("ı","i")#böylede kullanabiliriz
liste=list()
for x in "Python Co".replace("Co","a".capitalize()):
	liste.append(x);
	print(liste)