birinci_sayi=int(input("Birinci Sayı ?"))
ikinci_sayi=int(input("İkinci Sayı ?"))
üçüncü_sayi=int(input("Üçüncü Sayı ?"))
if birinci_sayi>ikinci_sayi and birinci_sayi>üçüncü_sayi:
    print(birinci_sayi)
elif ikinci_sayi>üçüncü_sayi and ikinci_sayi>üçüncü_sayi:
    print(ikinci_sayi)
elif üçüncü_sayi>ikinci_sayi and üçüncü_sayi>birinci_sayi:
    print(üçüncü_sayi)
