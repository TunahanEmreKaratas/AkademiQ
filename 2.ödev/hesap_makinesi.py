def hesap_makinesi(sayi1,sayi2,islem):
    if islem == "+":
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    
    elif islem == "-":
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    
    elif islem == "*":
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    
    elif islem == "/":
        if sayi2 == 0:
            return " Bölme işleminde ikinci sayı 0 olamaz"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü"
    

sayi1 = float(input("Birinci sayı:"))
sayi2 = float(input("İkinci sayı:"))
islem = input("İşlem türünü seçiniz(+,-,*,/):")

print(hesap_makinesi(sayi1,sayi2,islem))