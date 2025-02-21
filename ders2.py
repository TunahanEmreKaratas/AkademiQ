faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = input("Lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade))


#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = "Emre"
metin = "Merhaba {name}".format(name=123)
print(metin)

#f-string
metin=f"Hoşgeldiniz {1+1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç Kredisi",10 , 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) # lenght
#print(krediler[3])=> hata verir

krediler.append("X kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"])
print(krediler)


#for 
#i=0 i<10

for i in range(10):
    print("xx")
    print(i)

print("********************")

for i in range(5,11):
    print(i)

print("********************")

for i in range(0,51,10):
    print(i)
print("*******************")
#for i in range(0.1,0.5):
#   print(i)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*********************")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(10):
    print(i)
    
#sonsuz döngü
i=0
while i<10:
    print("x")
    i=i+1
print("y")

print("*********************")

while True:
    print("x")
    break

print("*********************")

i=0
while i < len(krediler):
    if krediler[i] == "Konut Kredsi":
        break
    print(krediler[i])
    i+=1


#fonksiyonlar

fiyat = 100
indirim = 20
# defination define

def calculate():
    print(100-20)


def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

calculate()    
calculateWithParams(50,10)
calculateWithParams(100,30)


def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("*********************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"147.satır:{fonk1}")
print(f"148.satır:{fonk2}")
print("**********************")


# sınıflar => classlar
# modules
# paket yönetimi
# self => this

class Human:
    #built-in #consturctor #initianalize
    def __init__(self,name):        
        self.name=name
        print("Bir Human instance'i üretildi")
    
    def talk(self,sentence):        
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek 
human1 = Human("Emre")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Tunahan")
human2.talk("Selam")
human2.walk()
print(human2)
