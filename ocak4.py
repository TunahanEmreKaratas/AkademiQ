# Kullanıcıdan 5 adet sayı alarak liste oluşturma ve işlemler
numbers = []
for i in range(5):
    num = int(input(f"{i+1}. sayıyı girin: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
max_num = max(numbers)
min_num = min(numbers)

print(f"Liste: {numbers}")
print(f"Toplam: {total}, Ortalama: {average}, En büyük: {max_num}, En küçük: {min_num}")

# Kullanıcıdan kelimeler alarak ters sıralayan program
words = []
for i in range(5):
    word = input(f"{i+1}. kelimeyi girin: ")
    words.append(word)

words.reverse()
print("Ters sıralanmış liste:", words)

# Liste içindeki tekrar eden elemanları kaldıran program
def remove_duplicates(lst):
    return list(set(lst))

sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(sample_list)
print("Tekrar eden elemanlar kaldırıldı:", unique_list)