from tkinter import *
import tkinter
from tkinter import messagebox

top = Tk()
top.configure(background='skyblue')

L0 = Label(top, text="*************NUMBER CONVERSION CALCULATOR*************",
           fg="navy blue",
           font="Times").grid(row=0,column=2)
"""--------------------BINARY TO OTHERS-------------------"""
LB = Label(top,text="Binary To Others",
           fg="darkorange",
           font="Times").grid(row=1,column=1)
"""--------------------BINARY  TO  DECIMAL-------------------"""
L2=Label(top,text="Binary To Decimal  ",
         fg="red",
         font="Times").grid(row=2,column=0)
E2 = Entry(top,bd=5,bg='springgreen')
E2.grid(row=2,column=1)
E22=Entry(top,bd=5,bg='springgreen')
E22.grid(row=2,column=3)

def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        binary_to_decimal()
def binary_to_decimal():
    binary=str(E2.get())
    btd = int(binary, 2)
    E22.insert(0,btd)
def b_to_d():
    messagebox.showinfo("info binary to decimal","a binary number is a number codded by 0,1 which is a machine readable language decimal is normal system we use in daily life from 0-9 in decimal") 
A1= tkinter.Button(top, relief=RAISED,text ="information", command = b_to_d,fg='black')
A1.grid(row=2,column=6)

B2=tkinter.Button(top,relief=RAISED,text="Convert Binary to Decimal",fg='blue',command=abc)
B2.grid(row=2,column=2)
"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""---------------------BINARY  TO  OCTAL--------------------"""
L3=Label(top,text="Binary To Octal  ",
         fg="red",
         font="Times").grid(row=3,column=0)
E3 = Entry(top,bd=5,bg='springgreen')
E3.grid(row=3,column=1)
E33=Entry(top,bd=5,bg='springgreen')
E33.grid(row=3,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        binary_to_octal()
def binary_to_octal():
    binary=str(E3.get())
    bto= int(binary, 2)
    bto=oct(bto)
    str(bto)
    bto=bto[1:]
    E33.insert(0,bto)
def b2o():
   messagebox.showinfo("binary to octal ", "a binary is a meachine readable language with 0,1 octal is a number system")
B112 = tkinter.Button(top, relief=RAISED,text = "information", command =b2o,fg='black')
B112.grid(row=3,column=6)

B3=tkinter.Button(top,relief=RAISED,text="Convert Binary To Octal",fg='blue',command=abc)
B3.grid(row=3,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------BINARY TO HEXADECIMAL-------------------"""
L4=Label(top,text="Binary To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=5,column=0)
E4 = Entry(top,bd=5,bg='springgreen')
E4.grid(row=5,column=1)
E44=Entry(top,bd=5,bg='springgreen')
E44.grid(row=5,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        binary_to_hexadecimal()
def binary_to_hexadecimal():
    binary=str(E4.get())
    bth = int(binary, 2)
    bth=hex(bth)
    str(bth)
    bth=bth[2:]
    bth=bth.upper()
    E44.insert(0,bth)
def b2h():
   messagebox.showinfo("binary to hexadecimal", " a binary number is a computuer readable language it is 0,1 hexadecimal is a system more than 10 number ")
B113 = tkinter.Button(top, relief=RAISED,text = "information", command = b2h,fg='black')
B113.grid(row=5,column=6)

B4=tkinter.Button(top,relief=RAISED,text="Convert Binary To Hexadecimal",fg='blue',command=abc)
B4.grid(row=5,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------BINARY TO OTHERS COMPLETE---------------"""

"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------DECIMAL TO OTHERS-------------------"""
LD = Label(top,text="Decimal To Others",
           fg="darkorange",
           font="Times").grid(row=6,column=1)
"""--------------------DECIMAL  TO  BINARY-------------------"""
L5=Label(top,text="Decimal To Binary   ",
         fg="red",
         font="Times").grid(row=7,column=0)
E5 = Entry(top,bd=5,bg='plum')
E5.grid(row=7,column=1)
E55=Entry(top,bd=5,bg='plum')
E55.grid(row=7,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
       decimal_to_binary()
def decimal_to_binary():
    decimal=str(E5.get())
    dtb = int(decimal)
    dtb=bin(dtb)
    str(dtb)
    dtb=dtb[2:]
    E55.insert(0,dtb)
def d2b():
   messagebox.showinfo("deciaml to binary", "a decimal number is a common dailyuse language from 0to9 binary is a meachine readable language from 0,1")
B114= tkinter.Button(top, relief=RAISED,text = "information", command = d2b,fg='black')
B114.grid(row=7,column=6)
B5=tkinter.Button(top,relief=RAISED,text="Convert Binary to Decimal",fg='blue',command=abc)
B5.grid(row=7,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------DECIMAL   TO  OCTAL-------------------"""
L6=Label(top,text="Decimal To Octal  ",
         fg="red",
         font="Times").grid(row=8,column=0)
E6 = Entry(top,bd=5,bg='plum')
E6.grid(row=8,column=1)
E66=Entry(top,bd=5,bg='plum')
E66.grid(row=8,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        decimal_to_octal()

def decimal_to_octal():
    decimal=str(E6.get())
    dto=int(decimal)
    dto=oct(dto)
    str(dto)
    dto=dto[1:]
    E66.insert(0,dto)
def d2o():
   messagebox.showinfo("decimal to octal ", "decimal number range  from 0 to 9 Octal is fancy for Base Eight meaning eight symbols are used to represent all the quantities. They are 0, 1, 2, 3, 4, 5, 6, and 7.8 doesn't exist in Octal")
B115 = tkinter.Button(top, relief=RAISED,text = "information", command = d2o,fg='black')
B115.grid(row=8,column=6)


B6=tkinter.Button(top,relief=RAISED,text="Convert Decimal To Octal",fg='blue',command=abc)
B6.grid(row=8,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------DECIMAL TO HEXADECIMAL-------------------"""
L7=Label(top,text="Decimal To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=9,column=0)
E7 = Entry(top,bd=5,bg='plum')
E7.grid(row=9,column=1)
E77=Entry(top,bd=5,bg='plum')
E77.grid(row=9,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        decimal_to_hexadecimal()

def decimal_to_hexadecimal():
    decimal=str(E7.get())
    dth = int(decimal)
    dth=hex(dth)
    str(dth)
    dth=dth[2:]
    dth=dth.upper()
    E77.insert(0,dth)
def d2h():
   messagebox.showinfo("decimal to hexadecimal", "decimal system numbers range from 0-9 the hexadecimal system is Base Sixteen total list of symbols to use is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, and F")
B116 = tkinter.Button(top, relief=RAISED,text = "information", command = d2h,fg='black')
B116.grid(row=9,column=6)

B7=tkinter.Button(top,relief=RAISED,text="Convert Decimal To Hexadecimal",fg='blue',command=decimal_to_hexadecimal)
B7.grid(row=9,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------DECIMAL TO OTHERS COMPLETE---------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------OCTAL TO OTHERS-------------------"""
LO = Label(top,text="Octal To Others ",
           fg="darkorange",
           font="Times").grid(row=10,column=1)
"""--------------------OCTAL    TO   BINARY-------------------"""
L8=Label(top,text="Octal To Binary   ",
         fg="red",
         font="Times").grid(row=11,column=0)
E8 = Entry(top,bd=5)
E8.grid(row=11,column=1)
E88=Entry(top,bd=5)
E88.grid(row=11,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        octal_to_binary()

def octal_to_binary():
    octal=str(E8.get())
    otb = str(int(octal,8))
    otb=int(otb)
    otb=bin(otb)
    otb=otb[2:]
    E88.insert(0,otb)
def o2b():
   messagebox.showinfo("octal to  binary", "Octal is fancy for Base Eight meaning  They are 0, 1, 2, 3, 4, 5, 6, and 7. When we count up one from the 7 no 8 binary is machine readable language with 0,1")
B117 = tkinter.Button(top, relief=RAISED,text = "information", command = o2b,fg='black')
B117.grid(row=11,column=6)
B8=tkinter.Button(top,relief=RAISED,text="Convert Octal To Binary",fg='blue',command=abc)
B8.grid(row=11,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------OCTAL   TO   DECIMAL-------------------"""
L9=Label(top,text="Octal To Decimal  ",
         fg="red",
         font="Times").grid(row=12,column=0)
E9 = Entry(top,bd=5)
E9.grid(row=12,column=1)
E99=Entry(top,bd=5)
E99.grid(row=12,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
     octal_to_decimal()
def octal_to_decimal():
    octal=str(E9.get())
    otd= str(int(octal,8))
    E99.insert(0,otd)
def o2d():
   messagebox.showinfo("octal to decimal", "Octal is fancy for Base Eight They are 0, 1, 2, 3, 4, 5, 6, and 7.decimal numbers ranging from 0to9")
B118= tkinter.Button(top, relief=RAISED,text = "information", command = o2d,fg='black')
B118.grid(row=12,column=6)
B9=tkinter.Button(top,relief=RAISED,text="Convert Octal To Decimal",fg='blue',command=abc)
B9.grid(row=12,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------OCTAL TO HEXADECIMAL-------------------"""
L10=Label(top,text="Octal To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=13,column=0)
E10= Entry(top,bd=5)
E10.grid(row=13,column=1)
E101=Entry(top,bd=5)
E101.grid(row=13,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        octal_to_hexadecimal()

def octal_to_hexadecimal():
    octal=str(E10.get())
    oth = str(int(octal,8))
    oth=int(oth)
    oth=hex(oth)
    oth=oth[2:]
    oth=oth.upper()
    E101.insert(0,oth)
def o2h():
   messagebox.showinfo("octal to hexadecimal", "Octal is fancy for Base Eight They are 0, 1, 2, 3, 4, 5, 6, and 7.the hexadecimal system is Base Sixteen total list of symbols to use is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, and F")
B114 = tkinter.Button(top, relief=RAISED,text = "information", command = o2h,fg='black')
B114.grid(row=13,column=6)

B10=tkinter.Button(top,relief=RAISED,text="Convert Octal To Hexadecimal",fg='blue',command=abc)
B10.grid(row=13,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------OCTAL TO OTHERS COMPLETE---------------"""




"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------HEXADECIMAL TO OTHERS-------------------"""
LH = Label(top,text="Hexadecimal To Others ",
           fg="darkorange",
           font="Times").grid(row=14,column=1)
"""--------------------HEXADECIMAL TO  BINARY-------------------"""
L11=Label(top,text="Hexadecimal To Binary   ",
         fg="red",
         font="Times").grid(row=15,column=0)
E11= Entry(top,bd=5,bg='lightpink')
E11.grid(row=15,column=1)
E111=Entry(top,bd=5,)
E111.grid(row=15,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        hexadecimal_to_binary()

def hexadecimal_to_binary():
    hexadecimal=str(E11.get())
    htb = int(hexadecimal,16);
    htb=bin(htb)
    htb=htb[2:]
    E111.insert(0,htb)
def h2b():
   messagebox.showinfo("hexadecimal o binary", "he hexadecimal system is Base Sixteen total list of symbols to use is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, and F binary machine readable language as 0,1")
B115 = tkinter.Button(top, relief=RAISED,text = "information", command = h2b,fg='black')
B115.grid(row=15,column=6)
B11=tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal to Binary",fg='blue',command=abc)
B11.grid(row=15,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------HEXADECIMAL TO DECIMAL-------------------"""
L12=Label(top,text="Hexadecimal To Decimal  ",
         fg="red",
         font="Times").grid(row=16,column=0)
E12= Entry(top,bd=5,bg='lightpink')
E12.grid(row=16,column=1)
E121=Entry(top,bd=5)
E121.grid(row=16,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        hexadecimal_to_decimal()

def hexadecimal_to_decimal():
    hexadecimal=str(E12.get())
    htd=int(hexadecimal,16)
    E121.insert(0,htd)
def h2d():
   messagebox.showinfo("hexadecimal to decimal", "he hexadecimal system is Base Sixteen total list of symbols to use is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, and F decimal range from 0-9")
B116 = tkinter.Button(top, relief=RAISED,text = "information", command = h2d,fg='black')
B116.grid(row=16,column=6)
    
B12=tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal To Decimal",fg='blue',command=abc)
B12.grid(row=16,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------HEXADECIMAL TO  OCTAL-------------------"""
L13=Label(top,text="Hexadecimal To Octal  ",
         fg="red",
         font="Times").grid(row=17,column=0)
E13= Entry(top,bd=5,bg='lightpink')
E13.grid(row=17,column=1)
E131=Entry(top,bd=5)
E131.grid(row=17,column=3)
def abc():
    if((str(E2.get())=="")):
        messagebox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        hexadecimal_to_octal()

def hexadecimal_to_octal():
    hexadecimal=str(E13.get())
    hto =int(hexadecimal,16)
    hto=oct(hto)
    hto=hto[1:]
    E131.insert(0,hto)
def h2o():
   messagebox.showinfo("hexadecimal to octal", "Octal is fancy for Base Eight They are 0, 1, 2, 3, 4, 5, 6, and 7. The hexadecimal system is Base Sixteen total list of symbols to use is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, and F")                      
B117 = tkinter.Button(top, relief=RAISED,text = "information", command = h2o,fg='black')
B117.grid(row=17,column=6)
B13=tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal To Octal",fg='blue',command=hexadecimal_to_octal)
B13.grid(row=17,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------OCTAL TO OTHERS COMPLETE---------------"""

"""------------------TO RESET ALL ENTRIES---------------"""
def clear_textbox():
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
    E7.delete(0, END)
    E8.delete(0, END)
    E9.delete(0, END)
    E10.delete(0, END)
    E11.delete(0, END)
    E12.delete(0, END)
    E13.delete(0, END)
    #OUTPUT ENTIRES CLEAR
    E22.delete(0, END)
    E33.delete(0, END)
    E44.delete(0, END)
    E55.delete(0, END)
    E66.delete(0, END)
    E77.delete(0, END)
    E88.delete(0, END)
    E99.delete(0, END)
    E101.delete(0, END)
    E111.delete(0, END)
    E121.delete(0, END)
    E131.delete(0, END)

B14=Button(top, text='RESET ALL ENTRIES',fg='navyblue',command=clear_textbox)
B14.grid(row=24,column=0)
"""-------------TO RESET ALL ENTRIES ENDED---------------"""

def close_window (): 
    top.destroy()
B15=Button (top,text = "EXIT",fg='red',command=close_window)
B15.grid(row=24,column=3)
D=Label(top,text="Developed By:-")
D.grid(row=26,column=0)

D2=Label(top,text="Sukhvanth Singh")
D2.grid(row=26,column=1)

top.mainloop()
