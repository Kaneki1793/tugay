tercih=input("Sinema mı yoksa Tiyatro mu?:")
ogrenci=input("öğrenci misin?:")
ucret=0
indirim=0.5
if tercih=="sinema":
    ucret+=15
elif tercih=="tiyatro":
    ucret+=10
if ogrenci=="evet":
    ucret*=indirim

print(ucret)
