class quiz:
    def __init__(self,quiz_adi,quiz_secenekleri,quiz_cevaplar):
        self.quiz_adi=quiz_adi
        self.quiz_secenekleri=quiz_secenekleri
        self.quiz_cevaplar=quiz_cevaplar
    def check_answer(self,answer):
        return self.quiz_cevaplar==answer
    

class soru:
    def __init__(self,sorular):
        self.sorular=sorular
        self.puan=0
        self.index=0
    def get_sorular(self):
        return self.sorular[self.index]
    def display_soru(self):
        soru2=self.get_sorular()
        count=1
        print('Soru {}: {} '.format(self.index+1,soru2.quiz_adi))
        for i in soru2.quiz_secenekleri:
            print(f"{count}-{i}")
            count+=1
        answer=input("Cevap:")
        self.tahmin(answer)
        self.soru_yukle()
        
    def tahmin(self,answer):
        soru2=self.get_sorular()
        if soru2.check_answer(answer):
            self.puan+=1
        self.index+=1
    def soru_yukle(self):
        if len(self.sorular)==self.index:
            self.showScore()
        else:
            self.displayProgress()
            self.display_soru()
    def showScore(self):
        print(f"Score:{self.puan}")
    def displayProgress(self):
        butun_sorular=len(self.sorular)
        soru_numarası=self.index+1
        if(soru_numarası>butun_sorular):
            print("Quiz Bitti.")
        else:
            print(f" Soru {soru_numarası} of {butun_sorular}".center(100,"*"))
q1=quiz("en iyi",["s","s","s","s"],"s")
q2=quiz("en kötü",["s","s","s","s"],"s")
q3=quiz("süper",["s","s","s","s"],"s")

sorular=[q1,q2,q3]
soru12=soru(sorular)
soru12.soru_yukle()
