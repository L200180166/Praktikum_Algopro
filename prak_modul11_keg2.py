from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className='Kalkulator')
print ("Hello")
L = Label(my_app, text="")
L.grid(row=0, column=4)
L1 = Label(my_app, text="Angka 1")
L1.grid(row=0, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text="Angka 2")
L2.grid(row=1, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(row=1, column=1, columnspan=3)

def jumlah():
    "Menjumlah E1 dan E2"
    data1 = float(str1.get())
    data2 = float(str2.get())
    jml = data1 + data2
    hasill.config(text=jml)
def kurang():
    "Menjumlah E1 dan E2"
    data1 = float(str1.get())
    data2 = float(str2.get())
    jml = data1 - data2
    hasill.config(text=jml)
def kali():
    "Menjumlah E1 dan E2"
    data1 = float(str1.get())
    data2 = float(str2.get())
    jml = data1*data2
    hasill.config(text=jml)
def bagi():
    "Menjumlah E1 dan E2"
    data1 = float(str1.get())
    data2 = float(str2.get())
    jml = data1/data2
    hasill.config(text=jml)

B1 = Button(my_app, text="+", command=jumlah)
B1.grid(row=2, column=0)
B2 = Button(my_app, text="-", command=kurang)
B2.grid(row=2, column=1)
B3 = Button(my_app, text="x", command=kali)
B3.grid(row=2, column=2)
B4 = Button(my_app, text=":", command=bagi)
B4.grid(row=2, column=3)
L3 = Label (my_app, text='Hasil:')
L3.grid(row=3, column=0)
hasill = Label (my_app, text='0')
hasill.grid(row=3, column=1)

my_app.mainloop()
