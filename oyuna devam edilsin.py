while True:
    tugay = input("Oyuna devam ediyon mu(Evet/Hayır)?:")    
    if tugay == "evet":
        print("Devamkee")
        continue  
    elif tugay == "hayır":
        print("Oyun bitti gardaş")
        break
    else:
        print("Gerekli cevap ver(Evet/Hayır)(emir)?.:")
