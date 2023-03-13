import tkinter
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilename
import re
import math
gui = Tk()
gui.title("CodeM Ver 1.0 (Beta)")
# Unresizeble The Window
gui.resizable(0,0)
# fun choice file
def choice_file():
    global filename
    tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(filetypes=[("Excel files", "*.xlsx; *.xls")]) # show an "Open" dialog box and return the path to the selected file
    lab2.config(text = "بر روی انجام عملیات کلیک کنید")
# do
def do_file():
    class Headererror(Exception):
        pass
    try:
        df = pd.read_excel(filename)
        def meli(c):
            o = str(int(c))
            if len(o) < 10:
                while len(o) <  10:
                    o = '0' + o
            return o
        code_col = []
        for col in df.columns:
            if re.search(r'کد ملی', col) or re.search(r'کدملی', col):
                code_col.append(col)

        for header in code_col:
            lstcode = []
            lstcode.extend((df[header].values[:]))
            lstcode = filter(lambda i : True if not math.isnan(float(i)) else False, lstcode)
            lstcode = list(lstcode)
            for code in lstcode:
                df[header] = df[header].replace(code, meli(code))
        code_meli= pd.DataFrame(df, columns=code_col)
        if code_col == []:
            raise Headererror
        with pd.ExcelWriter(filename, mode="a") as writer:
            code_meli.to_excel(writer, index=False, sheet_name='کد ملی های اصلاح شده')
            lab2.config(text = "!عملیات با موفقیت انجام شد")
    except ValueError:
        lab2.config(text = "!این فایل قبلا بررسی شده است")
    except FileNotFoundError:
        lab2.config(text = "!شما هیچ فایلی را انتخاب نکرده اید")
    except PermissionError:
        lab2.config(text = "!برای انجام عملیات فایل را ببندید")
    except Headererror:
        lab2.config(text = "!سطر اول این فایل حاوی عنوان است")
    except:
        lab2.config(text = "در صورت بروز خطا با برنامه نویس تماس بگیرید")
# App Header
lab1 = Label( gui, text ="برنامه تصحیح کدملی", relief=FLAT, width=300, pady=15, font=('B Zar Bold',13))
lab1.pack()
# Selector File btn
B = tkinter.Button(gui, text ="انتخاب فایل",font=('B Zar',13),width=20,command=choice_file)
B.pack()
# Do it btn
C = tkinter.Button(gui, text ="انجام عملیات",font=('B Zar',13),width=20,command=lambda: [do_file()])
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