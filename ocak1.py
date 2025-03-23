# Kullanıcıdan veri alma
ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
doğum_yılı = int(input("Doğum yılınızı girin: "))

# Kullanıcıya mesaj gösterme
print(f"Merhaba {ad}! {yas} yaşındasın ve {doğum_yılı} yılında doğmuşsun.")

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri yapma ve ekrana yazdırma
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
çarpım = sayi1 * sayi2
if sayi2 != 0:
    bölüm = sayi1 / sayi2
else:
    bölüm = "Tanımsız (0'a bölme hatası)"

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {çarpım}")
print(f"Bölüm: {bölüm}")