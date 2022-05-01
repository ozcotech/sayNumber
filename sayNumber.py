birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def say(sayi):
    birlerbasamak = sayi % 10
    onlarbasamak = sayi // 10

    return onlar[onlarbasamak] + " " + birler[birlerbasamak]

sayi = int(input("İki Basamaklı Bir Sayı Giriniz: "))

print(say(sayi))