kac_tane=int(input("Kaç tane sayı girilsin?:"))
toplam=0
for sayilar in range(kac_tane):
    print(sayilar + 1)
    sayi = int(input(". sayıyı gir:"))
    toplam +=  sayi
print("toplamı",toplam)
