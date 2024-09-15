import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('калькулятор')
root['bg'] = '#248248255'
icon = PhotoImage(file='image.png')
root.iconphoto(False, icon)
root.geometry("275x315+750+280")
root.minsize(250, 300)
root.maxsize(1000, 1000)
root.update_idletasks()
root.resizable(True, True)


def zapis_chisla(chislo):
    vpravo = vivod.get()
    if vpravo == '0':
        vpravo = vpravo[1:]
    vivod.delete(0, tkinter.END)
    vivod.insert(0, vpravo + chislo)


def zamenaoperatii(zamena):
    vpravo = vivod.get()
    if vpravo[-1] in ('-', '+', '/', '*', '%', 'C', '+/-', '.', '='):
        vpravo = vpravo[:-1]
    vivod.delete(0, tkinter.END)
    vivod.insert(0, vpravo + zamena)


def button(chislo):
    return tkinter.Button(text=chislo, foreground="white",background='grey', bd=7, command=lambda: zapis_chisla(chislo))


def operatii(operatia):
    return tkinter.Button(text=operatia, bd=7,background='orange',foreground='white', command=lambda: zamenaoperatii(operatia))


def podschet():
    chislo = vivod.get()
    vivod.delete(0, tkinter.END)
    vivod.insert(0, eval(chislo))


def schet(schet):
    return tkinter.Button(text=schet, bd=7, command=podschet)


def clear_entry():
    vivod.delete(0, tkinter.END)
    vivod.insert(0, "0")
    return 0


def smena_znaka():
    try:
        value = int(vivod.get())
        vivod.delete(0, tkinter.END)
        vivod.insert(0, str(-value))
    except ValueError:
        pass


def procent():
    znachenie = vivod.get()
    try:

        number = float(znachenie)

        result = number / 100

        vivod.delete(0, tkinter.END)
        vivod.insert(0, result)
    except ValueError:
        pass


def tochka():
    tekushee = vivod.get()
    tekushee += '.'
    vivod.delete(0, tkinter.END)
    vivod.insert(0, tekushee)


vivod = tkinter.Entry(root, justify=tkinter.RIGHT, background='#248248255', foreground='white', font=('Times New Roman', 30), width=10)
vivod.insert(0, '0')
vivod.grid(row=0, column=1, columnspan=4, ipadx=30, padx=5, pady=5, stick='we')
tkinter.Button(text="C",bd=7, command=clear_entry).grid(row=1, column=1, columnspan=1, padx=5, pady=5, stick="wens")
tkinter.Button(text="+/-",bd=7, command=smena_znaka).grid(row=1, column=2, columnspan=1, padx=5, pady=5, stick="wens")
tkinter.Button(text="%",bd=7, command=procent).grid(row=1, column=3, columnspan=1, padx=5, pady=5, stick="wens")
operatii("/").grid(row=1, column=4, columnspan=1, padx=5, pady=5, stick="wens")
operatii("*").grid(row=2, column=4, columnspan=1, padx=5, pady=5, stick="wens")
operatii("-").grid(row=3, column=4, columnspan=1, padx=5, pady=5, stick="wens")
operatii("+").grid(row=4, column=4, columnspan=1, padx=5, pady=5, stick="wens")
tkinter.Button(text=".", bd=7, command=tochka).grid(row=5, column=3, columnspan=1, padx=5, pady=5, ipady=10, stick="wens")
schet("=").grid(row=5, column=4, columnspan=1, padx=5, pady=5, ipady=10, stick="wens")
button('7').grid(row=2, column=1, columnspan=1, padx=5, pady=5, stick="wens")
button('8').grid(row=2, column=2, columnspan=1, padx=5, pady=5, stick="wens")
button('9').grid(row=2, column=3, columnspan=1, padx=5, pady=5, stick="wens")
button('4').grid(row=3, column=1, columnspan=1, padx=5, pady=5, stick="wens")
button('5').grid(row=3, column=2, columnspan=1, padx=5, pady=5, stick="wens")
button('6').grid(row=3, column=3, columnspan=1, padx=5, pady=5, stick="wens")
button('1').grid(row=4, column=1, columnspan=1, padx=5, pady=5, stick="wens")
button('2').grid(row=4, column=2, columnspan=1, padx=5, pady=5, stick="wens")
button('3').grid(row=4, column=3, columnspan=1, padx=5, pady=5, stick="wens")
button('0').grid(row=5, column=1, columnspan=2, ipadx=40, ipady=10, padx=5, pady=5, stick="wens")

root.mainloop()
