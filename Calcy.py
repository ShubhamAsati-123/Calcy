from tkinter import *
import math as m

large_font = ('arial',25)
small_font = ('arial',15)
ds = u"\N{DEGREE SIGN}"
sup_x = "ˣ"

def fact(n):
    fac = 1
    while n>0:
        fac *= n
        n -= 1
    return fac

def degree(n):
    l = n.split(ds)
    l[1:3] = l[1].split("\'")
    r = 0
    while "" in l:
        l.remove("")
    if len(l)==1:
        r = int(l[0])
        r = m.radians(r)
    elif len(l)==2:
        r = int(l[0]) + int(l[1])/60
        r = m.radians(r)
    elif len(l)==3:
        r = int(l[0]) + int(l[1])/60 + int(l[2])/60
        r = m.radians(r)
    scvalue.set(r)
    e1.update()

def radian(n):
    r = m.degrees(n)
    scvalue.set(r)
    e1.update()

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(e1.get())
            except Exception as e:
                value = 'Error'

        scvalue.set(value)
        e1.update()
        
    elif text == "C":
        scvalue.set("")
        e1.update()
    elif text == 'sin':
        value = str(m.sin(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'cos':
        value = str(m.cos(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'tan':
        value = str(m.tan(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'arcsin':
        value = str(m.asin(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'arccos':
        value = str(m.acos(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'arctan':
        value = str(m.atan(float(scvalue.get())))
        scvalue.set(value)
        e1.update()
    elif text == 'π':
        scvalue.set(str(m.pi))
        e1.update()
    elif text == 'e':
        scvalue.set(str(m.e))
        e1.update()
    elif text == 'Sqrt':
        scvalue.set(m.sqrt(float(scvalue.get())))
        e1.update()
    elif text == 'ln':
        scvalue.set(m.log(float(scvalue.get())))
        e1.update()
    elif text == 'log10':
        scvalue.set(m.log10(float(scvalue.get())))
        e1.update()
    elif text == 'n!':
        scvalue.set(fact(float(scvalue.get())))
        e1.update()
    elif text == '|x|':
        scvalue.set(abs(float(scvalue.get())))
        e1.update()
    elif text == '10'+sup_x:
        scvalue.set(10**float(scvalue.get()))
        e1.update()
    elif text == 'e'+sup_x:
        scvalue.set(m.e**float(scvalue.get()))
        e1.update()
    elif text == 'π'+sup_x:
        scvalue.set(m.pi**float(scvalue.get()))
        e1.update()
    elif text == '1/x':
        scvalue.set(1/float(scvalue.get()))
        e1.update()
    elif text == 'rad':
        a = degree(str(scvalue.get()))
    elif text == 'deg':
        scvalue.set(m.degrees(float(scvalue.get())))
        e1.update()
    elif text == 'CE':
        e1.delete("END")
        e1.update()
    else:
        scvalue.set(scvalue.get() + text)
        e1.update

win = Tk()
win.geometry('400x324')
win.title('Scientific Calculator by Shubham')

#Menu
main_menu = Menu(win)
new_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=new_menu)
new_menu.add_command(label="Scientific Calculator")
new_menu.add_command(label="Simple Calculator")
new_menu.add_command(label="Save")
new_menu.add_command(label="Save As")
new_menu.add_command(label="Exit", command=quit)

new_menu1 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=new_menu1)
new_menu1.add_command(label="Cut")
new_menu1.add_command(label="Copy")
new_menu1.add_command(label="Paste")
new_menu1.add_command(label="Delete")
win.config(menu=main_menu)

#Entry Widget
scvalue = StringVar()
scvalue.set("")
e1 = Entry(win, textvar=scvalue , font=large_font, width=22)
e1.grid(column=0, row=0, columnspan=6)

#Buttons Widget
l = Button(win, text='1', font=small_font, height = 1, width = 5)
l.grid(column=1, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='2', font=small_font, height = 1, width = 5)
l.grid(column=2, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='3', font=small_font, height = 1, width = 5)
l.grid(column=3, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='4', font=small_font, height = 1, width = 5)
l.grid(column=1, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='5', font=small_font, height = 1, width = 5)
l.grid(column=2, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='6', font=small_font, height = 1, width = 5)
l.grid(column=3, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='7', font=small_font, height = 1, width = 5)
l.grid(column=1, row=5)
l.bind('<Button-1>', click)
l = Button(win, text='8', font=small_font, height = 1, width = 5)
l.grid(column=2, row=5)
l.bind('<Button-1>', click)
l = Button(win, text='9', font=small_font, height = 1, width = 5)
l.grid(column=3, row=5)
l.bind('<Button-1>', click)
l = Button(win, text='C', font=small_font, height = 1, width = 5)
l.grid(column=0, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='CE', font=small_font, height = 1, width = 5)
l.grid(column=1, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='0', font=small_font, height = 1, width = 5)
l.grid(column=2, row=6)
l.bind('<Button-1>', click)
l = Button(win, text="=", font=small_font, height = 1, width = 5)
l.grid(column=4, row=7)
l.bind('<Button-1>', click)
l = Button(win, text='+', font=small_font, height = 1, width = 5)
l.grid(column=4, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='-', font=small_font, height = 1, width = 5)
l.grid(column=4, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='*', font=small_font, height = 1, width = 5)
l.grid(column=4, row=5)
l.bind('<Button-1>', click)
l = Button(win, text='/', font=small_font, height = 1, width = 5)
l.grid(column=4, row=6)
l.bind('<Button-1>', click)
l = Button(win, text='**', font=small_font, height = 1, width = 5)
l.grid(column=0, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='Sqrt', font=small_font, height = 1, width = 5)
l.grid(column=1, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='.', font=small_font, height = 1, width = 5)
l.grid(column=2, row=7)
l.bind('<Button-1>', click)
l = Button(win, text='e', font=small_font, height = 1, width = 5)
l.grid(column=3, row=6)
l.bind('<Button-1>', click)
l = Button(win, text='sin', font=small_font, height = 1, width = 5)
l.grid(column=2, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='cos', font=small_font, height = 1, width = 5)
l.grid(column=3, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='tan', font=small_font, height = 1, width = 5)
l.grid(column=4, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='π', font=small_font, height = 1, width = 5)
l.grid(column=3, row=7)
l.bind('<Button-1>', click)
l = Button(win, text='arcsin', font=small_font, height = 1, width = 5)
l.grid(column=2, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='arccos', font=small_font, height = 1, width = 5)
l.grid(column=3, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='arctan', font=small_font, height = 1, width = 5)
l.grid(column=4, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='(', font=small_font, height = 1, width = 5)
l.grid(column=0, row=6)
l.bind('<Button-1>', click)
l = Button(win, text=ds, font=small_font, height = 1, width = 5)
l.grid(column=0, row=7)
l.bind('<Button-1>', click)
l = Button(win, text='\'', font=small_font, height = 1, width = 5)
l.grid(column=1, row=7)
l.bind('<Button-1>', click)
l = Button(win, text='n!', font=small_font, height = 1, width = 5)
l.grid(column=0, row=5)
l.bind('<Button-1>', click)
l = Button(win, text=')', font=small_font, height = 1, width = 5)
l.grid(column=1, row=6)
l.bind('<Button-1>', click)
l = Button(win, text='ln', font=small_font, height = 1, width = 5)
l.grid(column=0, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='log10', font=small_font, height = 1, width = 5)
l.grid(column=0, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='|x|', font=small_font, height = 1, width = 5)
l.grid(column=5, row=1)
l.bind('<Button-1>', click)
l = Button(win, text='10'+sup_x, font=small_font, height = 1, width = 5)
l.grid(column=5, row=2)
l.bind('<Button-1>', click)
l = Button(win, text='e'+sup_x, font=small_font, height = 1, width = 5)
l.grid(column=5, row=3)
l.bind('<Button-1>', click)
l = Button(win, text='π'+sup_x, font=small_font, height = 1, width = 5)
l.grid(column=5, row=4)
l.bind('<Button-1>', click)
l = Button(win, text='1/x', font=small_font, height = 1, width = 5)
l.grid(column=5, row=5)
l.bind('<Button-1>', click)
l = Button(win, text='deg', font=small_font, height = 1, width = 5)
l.grid(column=5, row=6)
l.bind('<Button-1>', click)
l = Button(win, text='rad', font=small_font, height = 1, width = 5)
l.grid(column=5, row=7)
l.bind('<Button-1>', click)

win.mainloop()
