# Kullanıcının girdiği sayının tek mi çift mi olduğunu belirleme
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print(f"{sayi} çift sayıdır.")
else:
    print(f"{sayi} tek sayıdır.")

# Kullanıcının notunu alıp harf notunu belirleme
notu = int(input("Notunuzu girin: "))
if 90 <= notu <= 100:
    harf = "A"
elif 80 <= notu < 90:
    harf = "B"
elif 70 <= notu < 80:
    harf = "C"
elif 60 <= notu < 70:
    harf = "D"
else:
    harf = "F"
print(f"Harf notunuz: {harf}")

# Kullanıcının yaşına göre yaş grubunu belirleme
yas = int(input("Yaşınızı girin: "))
if yas <= 12:
    yas_grubu = "Çocuk"
elif 13 <= yas <= 19:
    yas_grubu = "Genç"
elif 20 <= yas <= 59:
    yas_grubu = "Yetişkin"
else:
    yas_grubu = "Yaşlı"
print(f"Yaş grubunuz: {yas_grubu}")