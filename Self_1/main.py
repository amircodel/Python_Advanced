import tkinter
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilename
import re
gui = Tk()
gui.title("Ver 1.0 (Beta)")
# Unresizeble The Window
gui.resizable(0,0)
# fun choice file
def choice_file():
    global filename
    tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(filetypes=[("Excel files", "*.xlsx; *.xls")]) # show an "Open" dialog box and return the path to the selected file
    lab2.config(text = "بر روی انجام عملیات کلیک کنید")
def do_file():
    global FNFE
    try:
        with open(filename, "w") as file:
            pass
    except FileNotFoundError:
        FNFE = lambda: lab2.config(text = "!شما هیچ فایلی را انتخاب نکرده اید")
# App Header
lab1 = Label( gui, text ="برنامه تصحیح کدملی", relief=FLAT, width=300, pady=15, font=('B Zar Bold',13))
lab1.pack()
# Selector File btn
B = tkinter.Button(gui, text ="انتخاب فایل",font=('B Zar',13),width=20,command=choice_file)
B.pack()
# Do it btn
C = tkinter.Button(gui, text ="انجام عملیات",font=('B Zar',13),width=20,command=lambda: [do_file(), FNFE()])
C.pack(pady=10)
# Description of the situation(2 choices)
lab2 = Label( gui,text = "یک فایل به فرمت اکسل انتخاب کنید", relief=FLAT, font=('B Zar',13),pady=-10)
lab2.pack()
B.pack()
# Footer
s= 'U+2665'
label = Label( gui, text="Powered by AmirAli Mohammadi with %c"%(chr(int(s[2:], 16))), relief=FLAT, font=('Times New Roman',10),pady=100)
label.pack()
gui.geometry("300x250")
gui.mainloop()