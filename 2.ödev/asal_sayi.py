def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} asal bir sayı değildir."
    for i in range(2,int(sayi**0.5)+1):
        if sayi%i==0:
            return f"{sayi} asal bir sayı değildir."
        
    return f"{sayi} asal bir sayıdır."

sayi = int(input("Bir sayı girin"))
print(asal_mi(sayi))