with open("metin.txt","w",encoding="utf-8") as file:
    metin = input("Bir metin girin:")
    file.write(metin)

with open("metin.txt","r",encoding="utf-8") as file:
    icerik = file.read()
    print("\nDosya içeriği:")
    print(icerik)

with open("veriler.txt","w",encoding="utf-8") as file:
    print("\n5 farklı satır verisi girin:")
    for i in range(5):
        satir = input(f"{i+1}.satırı girin:")
        file.write(satir + "\n")

print("\nDosyadaki Satırlar:")
with open("veriler.txt","r",encoding = "utf-8") as file:
    for satir in file:
        print(satir.strip())