sayac=0
while True:
    sifre=input("Bir şifre yazınız:")
    sayac+=1
    if(sifre == "KanekiKen"):
        print("Girişiniz yapıldı.")
        print(sayac,"tekrarda girişiniz yapıldı.")
        break
    print("Tekrar dene.")
    
