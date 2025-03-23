# Hesap makinesi fonksiyonu
def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme hatası)"
    return toplam, fark, carpim, bolum

s1 = float(input("Birinci sayıyı girin: "))
s2 = float(input("İkinci sayıyı girin: "))
sonuclar = hesap_makinesi(s1, s2)
print(f"Toplam: {sonuclar[0]}, Fark: {sonuclar[1]}, Çarpım: {sonuclar[2]}, Bölüm: {sonuclar[3]}")

# Palindrom kontrolü yapan fonksiyon
def palindrom_mu(kelime):
    return kelime == kelime[::-1]

kelime = input("Bir kelime girin: ")
if palindrom_mu(kelime):
    print(f"{kelime} bir palindromdur.")
else:
    print(f"{kelime} bir palindrom değildir.")

# 100 yaşına kaç yıl kaldığını hesaplayan fonksiyon
def kac_yil_sonra_100(yas):
    return 100 - yas if yas < 100 else 0

kullanici_yas = int(input("Yaşınızı girin: "))
kalan_yil = kac_yil_sonra_100(kullanici_yas)
print(f"100 yaşına {kalan_yil} yıl sonra ulaşacaksınız.")