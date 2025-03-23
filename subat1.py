# Kullanıcıdan 5 adet sayı alarak bir listeye ekleme
sayilar = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

# Liste işlemleri
toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

# Kullanıcıdan kelimeler alarak bir listeye ekleme ve ters sıralama
kelimeler = []
n = int(input("Kaç kelime gireceksiniz? "))
for i in range(n):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()
print("Ters sıralanmış kelimeler:", kelimeler)

# Bir liste içindeki tekrar eden elemanları kaldırma
orijinal_liste = [int(x) for x in input("Liste elemanlarını aralarında boşluk olacak şekilde girin: ").split()]
tekrarsiz_liste = list(set(orijinal_liste))
print("Tekrarsız liste:", tekrarsiz_liste)
