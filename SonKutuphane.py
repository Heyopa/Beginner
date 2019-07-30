import os
roman  = []
hikaye = []
bilim  = []
tarih  = []
kitapListe = [roman,hikaye,bilim,tarih]

menu = """
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kütüphane
[Q] Çıkış
"""
icmenu = """
[1] Roman
[2] Hikaye
[3] Bilim
[4] Tarih
[R]
"""
listemenu = """
[1] Roman
[2] Hikaye
[3] Bilim
[4] Tarih
[5] Tümünü listele
[R]
"""


def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Kitap Ekleme Başarıyla Gerçekleşti!")
    print("Menüye dönmek için 'Enter' tuşuna basınız!")
    input()
def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
def kitapCıkar(kitap:tuple,liste:list):
    if kontrol(True):
        liste.remove(kitap)
        print("Kitap Çıkartma Başarıyla Gerçekleşti!")
        print("Menüye dönmek için 'Enter' tuşuna basınız!")
        input()
    else:
        print("Kitap bulunamadı. Kontrol edip tekrar deneyiniz!")
        print("'Enter'a basarak tekrar yazabilirsiniz!")
        input()
def listele(liste:list):
    for i in liste:
        print("Kitap adı:{} ".format(i[0]), "Yazarı: {}".format(i[1]))
    print("Menüye dönmek için 'Enter' tuşuna basınız!")
    input()
while True:
    os.system("cls")
    print(menu)
    secim = input("Bir alan seçiniz: ")
    if secim == "1":
        while True:
            print(icmenu)
            tur = input("Bir tür seçiniz: ")
            if tur == "1":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim,yazar_isim)
                kitapEkle(kitap, roman)
            elif tur == "2":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapEkle(kitap, hikaye)
            elif tur == "3":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapEkle(kitap, bilim)
            elif tur == "4":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapEkle(kitap, tarih)
            elif tur == "r" or tur == "R":
                break
            else:
                print("Yanlış girdiniz")
                print("Menüye dönmek için 'Enter'a basınız!")

    elif secim == "2":
        while True:
            print(icmenu)
            tur = input("Bir tür seçiniz: ")
            if  tur == "1":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapCıkar(kitap, roman)
            elif tur == "2":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapCıkar(kitap, hikaye)
            elif tur == "3":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapCıkar(kitap, bilim)
            elif tur == "4":
                kitap_isim = input("Kitap adı: ")
                yazar_isim = input("Yazar adı: ")
                kitap = (kitap_isim, yazar_isim)
                kitapCıkar(kitap, tarih)
            elif tur == "q" or tur == "Q":
                break
            else:
                print("Hatalı Girdi!")
                print("Menüye dönmek için 'Enter'a basınız")
                input()
    elif secim == "3":
        while True:
            print(listemenu)
            tur = input("Bir tür seçiniz: ")
            if   tur == "1":
                print(roman)
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
            elif tur == "2":
                print(hikaye)
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
            elif tur == "3":
                print(bilim)
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
            elif tur == "4":
                print(tarih)
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
            elif tur == "5":
                print(kitapListe)
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
            elif tur == "r" or tur == "R":
                break
            else:
                print("Yanlış değer girdiniz!")
                print("Menüye dönmek için 'Enter' tuşuna basınız!")
                input()
    elif secim == "q" or secim == "Q":
            print("Programdan çıkış yapılıyor!")
            quit()
    else:
        print("Hatalı bir değer girdiniz!")
        print("Ana menüye dönmek için 'Enter' tuşuna basınız")
        input()









