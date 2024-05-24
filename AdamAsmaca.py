import random
from tkinter import *
from PIL import ImageTk, Image
import re
from tkinter import messagebox

def kelimeLimitle(*args):
    value = strValue.get()
    strValue.set(value.upper())
    if len(value) > 1: strValue.set(value[:1])
    if not re.match(r"^[A-Za-zğĞüÜşŞıİöÖçÇ]+$", value):
        strValue.set("")

def kontrol(panel, oldsayac):
    global sayac
    global rnd
    global bilinenler
    harf = strValue.get().upper()
    if harf == "":
        messagebox.showinfo("Bilgi", "Lütfen harf giriniz.")
    else:
        if harf in liste[rnd]:
            if harf not in bilinenler:
                bilinenler.append(harf)
            print(bilinenler)
            x = ""

            for harf in liste[rnd]:
                if harf in bilinenler:
                    x += harf + "    "
                else:
                    x += "_    "

            L1 = Label(window, text=x)
            L1.place(x=30, y=150)
            strValue.set('')
            if "_" not in x:
                messagebox.showinfo("Bilgi", "Kazandınız.")
                window.destroy()
        else:
            sayac = oldsayac + 1
            if sayac > 6:
                messagebox.showinfo("Bilgi", "Hakkınız bitti kaybettiniz.")
                window.destroy()
            else:
                img = ImageTk.PhotoImage(Image.open("images/"+str(sayac)+".png"))
                panel.configure(image=img)
                panel.image = img
                strValue.set('')

sayac = 0
bilinenler = []

#Kelime listesi
liste = ["SÜSLÜ", "EKRAN", "TABLO", "VERİTABANI", "MASA", "ÇİÇEK", "KAHVE", "YAZILIM", "TELEFON", "BİLİŞİM"]
###############

#Rastgele kelime seçimi
rnd = random.randint(0, len(liste) - 1)
print(liste[rnd])
#######################

window = Tk()

window.resizable(False, False)

window.title("Adam Asmaca")
window.geometry("400x250")

L1 = Label(window, text="Harf Girin:")
L1.place(x=50, y=15)

strValue = StringVar()
strValue.trace('w', kelimeLimitle)

E1 = Entry(window, width=6, textvariable=strValue)
E1.place(x=120,y=15)

img = ImageTk.PhotoImage(Image.open("images/"+str(sayac)+".png"))
panel = Label(window, image = img)
panel.place(x=220, y=10)

bt = Button(window, text="Kontrol Et", padx="50",pady="2", command=lambda: kontrol(panel, sayac))
bt.place(x=30,y=40)

#Kelimenin harf sayısı kadar _ koyan kod
x = ""

for i in range(len(liste[rnd])):
    x = x + "_    "

L1 = Label(window, text=x)
L1.place(x=30, y=150)
########################################

window.mainloop()