import random
from tkinter import *

liste = ["Süslü", "Ekran", "Tablo", "Veritabanı","Masa","Çiçek","Kahve","Yazılım","Telefon","Bilişim"]
rnd = random.randint(0, len(liste) - 1)
print(liste[rnd])



window = Tk()
window.title("Adam Asmaca")
window.geometry("400x250")
L1 = Label(window, text="Harf Girin:")
L1.place(x=30, y=15)

def limitSizeDay(*args):
    value = dayValue.get()
    if len(value) > 1: dayValue.set(value[:1])

dayValue = StringVar()
dayValue.trace('w', limitSizeDay)

E1 = Entry(window, width=6, textvariable=dayValue)
E1.place(x=30,y=45)

bt = Button(window, text="Kontrol Et", padx="2",pady="2")
bt.place(x=100,y=45)

window.mainloop()
