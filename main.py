from tkinter import *

# Window Settings
window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

# Uzunluk
label_length = Label(text="Enter your height ")
label_length.pack()

y_height = Entry(width=20)
y_height.pack()

# Ağırlık
label_weight = Label(text="Enter your weight ")
label_weight.pack()

y_weight = Entry(width=20)
y_weight.pack()

def button_clicked():
    global sonucu_yaz
    try:
        boy = int(y_height.get())
        agirlik = int(y_weight.get())
        sonuc = int(10000 * (agirlik / (boy * boy)))

        if 0 < sonuc < 18.5:
            sonucu_yaz.config(text="Aşırı zayıf")
        elif 18.5 <= sonuc < 24.9:
            sonucu_yaz.config(text="Normal")
        elif 25 <= sonuc < 29.9:
            sonucu_yaz.config(text="Biraz kilolu")
        elif 30 <= sonuc < 34.9:
            sonucu_yaz.config(text="Obezite başlangıcı")
        elif 35 <= sonuc < 39.9:
            sonucu_yaz.config(text="Obezite 2.sınıf")
        elif sonuc >= 40:
            sonucu_yaz.config(text="Obezite tedavi gerekiyor.")
        '''else:
            print("Geçersiz değerler. Lütfen boy ve kilo değerlerini kontrol edin.") '''
    except ValueError:
        print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")
    #print("Vücut Kitle İndeksi:", sonuc)


Calculate_Button = Button(text="Calculate", command=button_clicked)
Calculate_Button.pack()

# Sonuç
sonucu_yaz = Label(text=" ")
sonucu_yaz.pack()

window.mainloop()
