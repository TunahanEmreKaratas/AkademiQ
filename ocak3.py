# 1'den 100'e kadar olan sayıları ekrana yazdırma
for i in range(1, 101):
    print(i, end=' ')
print()

# 1'den 100'e kadar sadece çift sayıları ekrana yazdırma
for i in range(2, 101, 2):
    print(i, end=' ')
print()

# Kullanıcının girdiği sayının faktöriyelini hesaplama
sayi = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")

# 1'den 100'e kadar olan tüm asal sayıları bulma
print("1'den 100'e kadar olan asal sayılar:")
for num in range(2, 101):
    asal = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            asal = False
            break
    if asal:
        print(num, end=' ')
print()