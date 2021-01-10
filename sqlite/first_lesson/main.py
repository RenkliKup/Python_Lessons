import sqlite3 as sql


vt=sql.connect("first_db.sqlite")#veri tabanına bağlanır eğer veri tabanı yoksa yoktan var eder

imlec=vt.cursor() #veri tabanında islem yapmamızı sağlar
imlec.execute("CREATE TABLE IF NOT EXISTS kitap_bilgisi (kitap_adi,kitap_yazari,okunma_durumu,begeni)")
#kitap_bilgisi adında bir tablo oluşturuyoruz ve satırlarını kitap_adi kitap_yazari,okunma_durumu,begeni yapıyoruz
#hata almamak için IF NOT EXISTS kontrolü 
kitap_girisi="INSERT INTO kitap_bilgisi VALUES ('Suç ve Ceza','Dostoyevski','evet','*****')"
imlec.execute(kitap_girisi)
vt.commit()#veri tabanı bilgisini kaydeder
vt.close() #veri tabanını kapatır