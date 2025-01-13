toplam=0
Sayac=0
while True:
    sayi = int(input("Sayı giriniz?:"))
    if sayi==1:
        break
    toplam+=sayi
    Sayac+=1

print("Ortalama",toplam/Sayac)

