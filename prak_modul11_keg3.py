from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'LUAS JAJARGENJANG')

D = Label(my_app, text ='LUAS JAJARGENJANG',font='TimesNewRoman 20 bold')
D.grid(row=0, column=0)

D1 = Label(my_app, text ='JAJARGENJANG adalah bangun 2 dimensi ''\nJAJARGENJANG memiliki 4 sisi,dan 4 titik sudut.',font='Chiller 15',)
D1.grid(columnspan=4,row=1, column=0)

L1 = Label (my_app, text = 'Parameter Sisi1 : ')
L1.grid(row=2, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(columnspan=3 ,row=2, column=1)

L2 = Label (my_app, text = 'Parameter Sisi2 : ')
L2.grid(row=3, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(columnspan=3 ,row=3, column=1)


def luas():
    s1=float(str1.get())
    s2=float(str2.get())
    luass=s1*s2
    LP.config(text=luass)

B = Button(my_app, text='Hitung Luas', command= luas)
B.grid(row=5,column=0)
L=Label(my_app, text='luas :',font='TimesNewRoman 15 bold')
L.grid(row=5,column=2)
LP=Label(my_app, text='0')
LP.grid(row=5,column=3)

my_app.mainloop()
