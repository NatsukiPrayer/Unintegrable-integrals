# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:30:06 2019

@author: Пафнутий
"""
LARGE_FONT=("Verdana", 12)
from decimal import Decimal
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from tkinter import *
from math import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog
import math as m
from matplotlib import style
import matplotlib.animation  as animation
from tkinter import scrolledtext
import scipy as scp
from scipy import integrate
import scipy.special as special
import os
style.use('ggplot')

funnc = lambda x: x**2 * m.sin(5*x)
funncc = lambda x: x**2 * m.cos(5*x)
'''
def Graphic():
    graph_window = Tk()
    graph_window.geometry('900x600')
    pullData = open("func.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x, y = eachLine.split(',')
            xList.append(x)
            yList.append(int(y))
    a.clear()
    a.plot(yList, xList, label = 'Первый метод')
    label = tk.Label(graph_window, text="Graph Page!")
    label.pack(pady=10, padx=10) 
    canvas = FigureCanvasTkAgg(f, graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
    toolbar = NavigationToolbar2Tk(canvas, graph_window)
    toolbar.update()
    canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
    graph_window.mainloop()
    a.set_title('POMOGITE')
    plt.legend()
 '''
       
def enter_clicked(border_l, border_u, func, parts):
    try:
        n = int(parts.get())
        l = int(border_l.get())
        u = int(border_u.get())
        fuc = func.get()
        if n < 1:
            raise  Exception
    except ValueError:
        messagebox.showerror('Ошибка','Неверный формат ввода!')
        return
    except Exception:
        messagebox.showerror('Ошибка','Невозможное колиество разбиений!')
        return
    if not parts.get():
        messagebox.showerror('Ошибка','Вы не ввели количество разбиений!')
        return
    if not func.get():
        messagebox.showerror("Ошибка", "Вы не выбрали функцию!")
        return
    f_values=[]
    f_par_values = []
    Sum = []
    Sum_par = []
    Summ = 0
    Summ_par = 0
    bords = []
    h=(u - l)/n
    if fuc == 'sin(5x)':
        real = Decimal((m.cos(5*u)/-5) + m.cos(5*l)/5)
        for i in range (0, n):
            if i == 0:
                pair = [((m.sin(l) + m.sin(u))*h)/2, i]
                f_values.append(pair)
                Summ+=pair[0]
            else:
                pair=[(m.sin(5*(l + i*h)))*h, i]        
                f_values.append(pair)
                Summ+=pair[0]
            Sum.append(Summ)
        for i in range (0, n):
            if i == 0:
                pair = [((m.sin(l) + m.sin(u))*h)/3, i]
                f_par_values.append(pair)
                Summ_par+=pair[0]
            elif (i%2) == 1:
                pair=[(m.sin(5*(l + i*h)))*4*h/3, i]        
                f_par_values.append(pair)
                Summ_par+=pair[0]
            elif (i%2) == 0:
                pair=[(m.sin(5*(l + i*h)))*2*h/3, i]        
                f_par_values.append(pair)
                Summ_par+=pair[0]
            Sum_par.append(Summ_par)
    elif fuc == 'x^2':
        real = Decimal(u**3/3 - l**3/3)
        for i in range (0, n):
            if i == 0:
                pair = [((l**2 + u**2)*h)/2, i]
                f_values.append(pair)
                Summ+=pair[0]
            else:
                pair=[(l + i*h)**2 * h, i]        
                f_values.append(pair)
                Summ+=pair[0]
            Sum.append(Summ)
        for i in range (0, n):
            if i == 0:
                pair = [((l**2 + u**2)*h)/3, i]
                f_par_values.append(pair)
                Summ_par+=pair[0]
            elif (i%2) == 1:
                pair=[(l + i*h)**2*4*h/3, i]        
                f_par_values.append(pair)
                Summ_par+=pair[0]
            elif (i%2) == 0:
                pair=[(l + i*h)**2*2*h/3, i]        
                f_par_values.append(pair)
                Summ_par+=pair[0]
            Sum_par.append(Summ_par)
    bords=[Sum, Sum_par, real, fuc, l, u, f_values, f_par_values]
    return bords

def proverka(border_l, border_u, func, parts):
    test = Tk()
    try:
        n = parts.get().split(',')
        l = float(border_l.get())
        u = float(border_u.get())
        fuc = func.get()
        for i in range (0, len(n)):
            if int(n[i]) < 1:
                raise  Exception
    except ValueError:
        messagebox.showerror('Ошибка','Неверный формат ввода!')
        return
    except Exception:
        messagebox.showerror('Ошибка','Невозможное колиество разбиений!')
        return
    if not parts.get():
        messagebox.showerror('Ошибка','Вы не ввели количество разбиений!')
        return
    if not func.get():
        messagebox.showerror("Ошибка", "Вы не выбрали функцию!")
        return
    n_new = []
    for i in range(0, len(n)):
        n_new.append(int(n[i]))
    n_new.sort()
    f_val_t=[]
    f_val_p=[]
    F_P = []
    F_T = []
    Par_meth = []
    Trap_meth = []
    for j in range (0, len(n)):
        Summ = 0
        Summ_par = 0
        h=(u - l)/n_new[j]
        print(h)
        if fuc == 'x^2sin(5x)':
            real_real = integrate.quad(funnc, l, u)
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = ((sin_f(l) + sin_f(u))*h)/2
                    f_val_t.append(pair)
                    Summ+=pair
                else:
                    pair=sin_f(l+(i*h))*h
                    f_val_t.append(pair)
                    Summ+=pair
            
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = (sin_f(l) + sin_f(u))*h/3
                    f_val_p.append(pair)
                    Summ_par+=pair
                elif (i%2) == 1:
                    pair=sin_f(l+(i*h))*4*h/3
                    f_val_p.append(pair)
                    Summ_par+=pair
                elif (i%2) == 0:
                    pair=sin_f(l+(i*h))*2*h/3       
                    f_val_p.append(pair)
                    Summ_par+=pair
        elif fuc == 'x^2cos(5x)':
            real_real = integrate.quad(funncc, l, u)
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = ((cos_f(l) + cos_f(u))*h)/2
                    f_val_t.append(pair)
                    Summ+=pair
                else:
                    pair=cos_f(l+(i*h))*h
                    f_val_t.append(pair)
                    Summ+=pair
            
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = (cos_f(l) + cos_f(u))*h/3
                    f_val_p.append(pair)
                    Summ_par+=pair
                elif (i%2) == 1:
                    pair=cos_f(l+(i*h))*4*h/3
                    f_val_p.append(pair)                        
                    Summ_par+=pair
                elif (i%2) == 0:
                    pair=cos_f(l+(i*h))*2*h/3       
                    f_val_p.append(pair)                    
                    Summ_par+=pair
        Par_meth.append(Summ_par)
        Trap_meth.append(Summ)
        F_P.append(f_val_p)
        F_T.append(f_val_t)
    t = tk.scrolledtext.ScrolledText(test, height = 50, width = 50)
    string = 'Истинное значение интеграла:' + str(real_real[0]) + '\n' 
    c = 28
    t.insert(1.0, string)
    for i in range(0, len(n_new)):
        if n_new[i] > 0:
            partit = 'n = ' + str(n_new[i]) +'\n'
            Itr = 'Itr = ' + str(round(Trap_meth[i],4)) + '\n'
            Ipar = 'Ipr = ' + str(round(Par_meth[i],4)) + '\n'
            test.geometry('360x280')
            t.insert(INSERT, partit)
            t.insert(c+2.0, Itr)
            t.insert(c+4.0, Ipar)
            c+=2
    """else:
            partit = 'n = ' + str(n_new[i]) + '\n'
            temp = ''
            temp_p =''
            for j in range (0, len(F_P[i])):
                if j != len(F_P[i])-1:
                    temp += str(round(F_T[i][j],4)) + ' + '
                    temp_p += str(round(F_P[i][j],4)) + ' + '
                else:
                    temp+=str(round(F_T[i][j],4))
                    temp_p+=str(round(F_P[i][j],4))
            Itr = 'Itr = ' + temp + '\n'
            Ipr = 'Ipr = ' + temp_p + '\n'
            t.insert(INSERT, partit)
            t.insert(c+2.0, Itr)
            t.insert(c+4.0, Ipr)
            c+=2
    """
    t.grid(column=0, row = 0)
    test.mainloop()

class SeaOfBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne):
        
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def file(func):
    if not func.get():
       return messagebox.showerror("Ошибка", "Вы не выбрали функцию!")
    messagebox.showinfo('Выбор файла', 'Файл должен быть с расширение .txt \nи иметь вид трёх колонок из цифр, разделённых запятой. \nПервая колонка воспринимается как количество разбиений, вторая как нижняя граница и третья как верхняя граница интегрирования')
    fucc = func.get()
    files = filedialog.askopenfilenames()
    print(files)
    file_name, file_ext= os.path.splitext(files[0])
    print(file_ext)
    print(type(files))
    if file_ext == '.txt':
      parts = ''
      fl = open(files[0], 'r')
      data = [line.split(',') for line in fl]
      for i in range(1, len(data)):
          if i != len(data)-1:
              parts += data[i][0] + ', '
          else:
              parts += data[i][0]
      partition.delete(0, END)
      partition.insert(0, parts)
      l = data[1][1]
      u = data[1][2]
      border_l.delete(0, END)
      border_l.insert(0, l)
      border_u.delete(0, END)
      border_u.insert(0, u)
    elif not file_ext:
      return messagebox.showerror('Ошибка','Файл не выбран!')
    else:
      return messagebox.showerror('Ошибка','Неверный формат файла!')
    
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller, bg = "black"):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Численное интегрирование", font = LARGE_FONT)
        label.grid(column = 0, row = 0)
        label1 = ttk.Label(self, text="Выберите функцию из списка:", font = LARGE_FONT)
        label1.grid(column = 0, row = 1)
        combo = Combobox(self)  
        combo['values'] = ('x^2sin(5x)', 'x^2cos(5x)')
        combo.grid(column = 0, row = 2)
        label2 = ttk.Label(self, text="Введите верхнюю границу интегрирования:", font = LARGE_FONT)
        label2.grid(column = 0, row = 7)
        label3 = ttk.Label(self, text="Введите нижнюю границу интегрирования:", font = LARGE_FONT)
        label3.grid(column = 0, row = 6)
        label4 = ttk.Label(self, text="Введите количество разбиений через запятую:", font = LARGE_FONT)
        label4.grid(column = 0, row = 5)
        global partition
        global border_l
        global border_u
        partition = Entry(self, width = 5,  bd = 3)
        partition.grid(column = 1, row = 5)
        border_l = Entry(self, width = 5, bd = 3)
        border_l.grid(column = 1, row = 6)
        border_u = Entry(self, width = 5,  bd = 3)
        border_u.grid(column = 1, row = 7)
        tk.Button(self,text="Построить график",command= lambda: draw_chart(border_l, border_u, combo, partition)).grid(column=0, row=8)
        enter1 = Button(self, text = 'Проверка', command = lambda: proverka(border_l, border_u, combo, partition))
        enter1.grid(column = 1, row = 8)
        enter2 = Button(self, text = 'Ввод из файла', command = lambda: file(combo))
        enter2.grid(column = 1, row = 9)
        #graphic = Button(self, text = 'Построить график', command = lambda: Graphic(enter_clicked(border_l, border_u, combo))[5])
        #graphic.grid(column = 1, row = 10)
        #btn1 = ttk.Button(self, text = 'Visit page 3', command = lambda:controller.show_frame(PageThree))
        #btn1.grid(column = 0, row = 3)
        #btn3 = ttk.Button(self, text = 'Visit page 1', command = lambda:controller.show_frame(PageOne))
        #btn3.grid(column = 0, row = 4)
        #btn4 = ttk.Button(self, text = 'Visit graph page', command = lambda:controller.show_frame(Graph_page))
        #btn4.grid(column = 1, row = 11)       
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font = LARGE_FONT)
        label.pack(pady=10, padx = 10)
        btn2 = ttk.Button(self, text = 'Back to Home', command = lambda:controller.show_frame(StartPage))
        btn2.pack()


def sin_f(x):
    return (x**2)*m.sin(5*x)
def cos_f(x):
    return (x**2)*m.cos(5*x)


def draw_chart(border_l, border_u, func, parts):
    try:
        n = parts.get().split(',')
        l = float(border_l.get())
        u = float(border_u.get())
        fuc = func.get()
        for i in range (0, len(n)):
            if int(n[i]) < 1:
                raise  Exception
    except ValueError:
        messagebox.showerror('Ошибка','Неверный формат ввода!')
        return
    except Exception:
        messagebox.showerror('Ошибка','Невозможное колиество разбиений!')
        return
    if not parts.get():
        messagebox.showerror('Ошибка','Вы не ввели количество разбиений!')
        return
    if not func.get():
        messagebox.showerror("Ошибка", "Вы не выбрали функцию!")
        return
    n_new = []
    for i in range(0, len(n)):
        n_new.append(int(n[i]))
    n_new.sort()
    print (n_new)
    print(type(n_new[0]))
    root = Tk()
    root.title('График сходимости')
    root.geometry('800x600')
    fig = plt.figure(figsize=(5, 5), dpi=100)
    fig.show()
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand= True)
    toolbar = NavigationToolbar2Tk(canvas, root)
    f_values=[]
    fig.clear()
    Par_meth = []
    Trap_meth = []
    for j in range (0, len(n)):
        Summ = 0
        Summ_par = 0
        h=(u - l)/n_new[j]
        print(h)
        if fuc == 'x^2sin(5x)':
            real_real = integrate.quad(funnc, l, u)
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = ((sin_f(l) + sin_f(u))*h)/2
                    Summ+=pair
                else:
                    pair=sin_f(l+(i*h))*h
                    Summ+=pair
            
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = (sin_f(l) + sin_f(u))*h/3
                    Summ_par+=pair
                elif (i%2) == 1:
                    pair=sin_f(l+(i*h))*4*h/3
                    Summ_par+=pair
                elif (i%2) == 0:
                    pair=sin_f(l+(i*h))*2*h/3       
                    Summ_par+=pair
        elif fuc == 'x^2cos(5x)':
            real_real = integrate.quad(funncc, l, u)
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = ((cos_f(l) + cos_f(u))*h)/2
                    Summ+=pair
                else:
                    pair=cos_f(l+(i*h))*h
                    Summ+=pair
            
            for i in range (0, n_new[j]):
                if i == 0:
                    pair = (cos_f(l) + cos_f(u))*h/3
                    Summ_par+=pair
                elif (i%2) == 1:
                    pair=cos_f(l+(i*h))*4*h/3
                    Summ_par+=pair
                elif (i%2) == 0:
                    pair=cos_f(l+(i*h))*2*h/3       
                    Summ_par+=pair
        Par_meth.append(Summ_par)
        Trap_meth.append(Summ)
        t = np.linspace(0, n_new[j],2)        
    y0 = float(real_real[0]) + 0*t
    string = 'ист. знач.=' + str(float(round(real_real[0], 6)))
    fig.add_subplot(111).plot(t, y0, 'm--', label=string)
    fig.add_subplot(111).plot(n_new, Trap_meth, 'gx', label = 'Метод трапеций', markersize = 8)
    fig.add_subplot(111).plot(n_new, Par_meth, 'ro', label = 'Метод парабол', markersize = 8)
    canvas.draw_idle()
    plt.xlabel('n')
    plt.ylabel('Значение I')
    plt.title('График сходимости')
    plt.legend(loc='best')     
    plt.grid(True, color = 'black')
    plt.close(fig)                                                                
    #fig.add_subplot(1,1,2, sharex = True, sharey = True)
    #fig.add_subplot(1,1,3, sharex = True, sharey = True).plot(0.5, 14)
    #generate random x/y
    #fig.add_subplot(a_ss)
    #fig.align_xlabels(axs = 'Участок разбиения n')
    root.mainloop()

app = SeaOfBTCapp()
app.title('Численное интегрирование') 
#graph = Graph()
#ani = animation.FuncAnimation(f, Graphic, interval = 1000)
#graph.title('График сходимости методов')  
#graph.mainloop()
#app.bg("light-blue")
app.mainloop()

