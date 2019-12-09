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
import math as m
from matplotlib import style
import matplotlib.animation  as animation
from tkinter import scrolledtext
import scipy as scp
import scipy.integrate as integrate
import scipy.special as special
style.use('ggplot')


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

def proverka(l):
    test = Tk()
    result = integrate.quad(lambda x: x**2 * m.sin(5*x), 0, 4.5)
    print(result)
    if not l:
        messagebox.showerror('Ошибка', 'Неверный формат проверяемых данных!')
    elif len(l[0]) > 16:
        string = 'Вывод сокращён до суммы методов из-за большего числа разбиений\n' + 'Истинное значение интеграла:' + l[3] +'='
        if l[3] == 'sin(5x)':
            cos_l = round(m.cos(5*l[4])/5, 4)
            cos_u = round(m.cos(5*l[5])/5, 4)
            string+='-cos(5x)/5, верхняя граница= ' + str(l[4]) + ', нижняя граница= ' + str(l[5]) +'\nПодставляя имеем: ' + str(cos_u) + ' - ' + str(cos_l) + ' = ' + str(cos_u-cos_l) + '\n'
        elif l[3] == 'x^2':
            x_u = round(l[5]**3/3, 4)
            x_l = round(l[4]**3/3, 4)
            string+='x^3/3, верхняя граница= ' + str(l[4]) + ', нижняя граница= ' + str(l[5]) +'\nПодставляя имеем: ' + str(x_u)+ ' - ' + str(x_l) + ' = ' + str(x_u - x_l) + '\n'
        Itr = 'Для метода трапеций: Itr = ' + str(l[0][len(l[0])-1])
        Ipar = 'Для метода парабол: Itr = ' + str(l[1][len(l[1])-1])
        t = tk.scrolledtext.ScrolledText(test, height = 40, width = len(Itr))
        test.geometry('1440x280')
        t.insert(1.0, string)
        t.insert(5.0, Itr)
        t.insert(7.0, Ipar)
        t.grid(row=0, column=0)
    else:
        string = 'Истинное значение интеграла:' + l[3] +'='
        if l[3] == 'sin(5x)':
            cos_l = round(m.cos(5*l[4])/5, 4)
            cos_u = round(m.cos(5*l[5])/5, 4)
            string+='-cos(5x)/5, верхняя граница= ' + str(l[4]) + ', нижняя граница= ' + str(l[5]) +'\nПодставляя имеем: ' + str(cos_u) + ' - ' + str(cos_l) + ' = ' + str(cos_u-cos_l) + '\n'
        elif l[3] == 'x^2':
            x_u = round(l[5]**3/3, 4)
            x_l = round(l[4]**3/3, 4)
            string+='x^3/3, верхняя граница= ' + str(l[4]) + ', нижняя граница= ' + str(l[5]) +'\nПодставляя имеем: ' + str(x_u)+ ' - ' + str(x_l) + ' = ' + str(x_u - x_l) + '\n'
        Itr = 'Для метода трапеций:'
        for i in range(0, len(l[0])):
            if i == 0:
                Itr+=str(round(l[6][i][0], 4)) + ' +'
            elif i!= len(l[0])-1:
                Itr+=' ' + str(round(l[6][i][0],4)) + ' +'
            else:
                Itr+=' ' + str(round(l[6][i][0],4)) + '= ' + str(round(l[0][i], 4)) 
        Ipar = 'Для метода парабол:'
        for i in range(0, len(l[1])):
            if i == 0:
                Ipar+=str(round(l[7][i][0], 4)) + ' +'
            elif i!= len(l[1])-1:
                Ipar+=' ' + str(round(l[7][i][0],4)) + ' +'
            else:
                Ipar+=' ' + str(round(l[7][i][0],4)) + '= ' + str(round(l[1][i], 4)) 
        t = tk.scrolledtext.ScrolledText(test, height = 40, width = len(Itr))
        test.geometry('1440x280')
        t.insert(1.0, string)
        t.insert(5.0, Itr)
        t.insert(7.0, Ipar)
        t.grid(row=0, column=0)
        #string = 'Проверка' + str(l[0]) + '---' + str(l[1]) + '000  ' + str(l)
        #messagebox.showinfo('Проверка', string)
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

def sosi(p):
    print(p.get().split(' '))
    
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
        partition = Entry(self, width = 5,  bd = 3)
        partition.grid(column = 1, row = 5)
        border_l = Entry(self, width = 5, bd = 3)
        border_l.grid(column = 1, row = 6)
        border_u = Entry(self, width = 5,  bd = 3)
        border_u.grid(column = 1, row = 7)
        tk.Button(self,text="Построить график",command= lambda: draw_chart(border_l, border_u, combo, partition)).grid(column=0, row=8)
        enter1 = Button(self, text = 'Проверка', command = lambda: proverka(enter_clicked(border_l, border_u, combo, partition)))
        enter1.grid(column = 1, row = 8)
        enter2 = Button(self, text = 'Проверка т', command = lambda: sosi(partition))
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




def draw_chart(border_l, border_u, func, parts):
    n_1 = parts.get().split(',')
    for i in range (0, len(n_1)):
            if int(n_1[i]) < 1:
                print(n_1[i],'\notsosi')
    try:
        n = parts.get().split(',')
        l = int(border_l.get())
        u = int(border_u.get())
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
    for j in range (0, len(n)):
        Summ = 0
        Summ_par = 0
        h=(u - l)/int(n[j])
        if fuc == 'x^2sin(5x)':
            real = Decimal((2/125 - u**2/5)*cos(5*u) + 2/25*u*sin(5*u) - (2/125 - l**2/5)*cos(5*l) + 2/25*l*sin(5*l))
            for i in range (0, int(n[j])):
                if i == 0:
                    pair = [((l**2 * sin(l) + u**2 * sin(u))*h)/2, i]
                    f_values.append(pair)
                    Summ+=pair[0]
                else:
                    pair=[((l+i*h)**2 * sin(5*(l + i*h)))*h, i]        
                    f_values.append(pair)
                    Summ+=pair[0]
            
            for i in range (0, int(n[j])):
                if i == 0:
                    pair = [((l**2 * sin(l) + u**2 * sin(u))*h)/3, i]
                    f_values.append(pair)
                    Summ_par+=pair[0]
                elif (i%2) == 1:
                    pair=[((l+i*h)**2 * sin(5*(l + i*h)))*4*h/3, i]        
                    f_values.append(pair)
                    Summ_par+=pair[0]
                elif (i%2) == 0:
                    pair=[((l+i*h)**2 * sin(5*(l + i*h)))*2*h/3, i]        
                    f_values.append(pair)
                    Summ_par+=pair[0]
        
        t = np.linspace(0, int(n[j]),2)
        y0 = float(real) + 0*t
        string = 'ист. знач.=' + str(float(real.quantize(Decimal("1.00000"))))
        fig.add_subplot(111).plot(t, y0, 'm--', label=string)
        fig.add_subplot(111).plot(Summ, int(n[j]), 'gx', label = 'Метод трапеций', markersize = 8)
        fig.add_subplot(111).plot(Summ_par, int(n[j]), 'ro', label = 'Метод парабол', markersize = 8)
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
    print(Summ)
    print(Sum)
    print(real)
    root.mainloop()

app = SeaOfBTCapp()
app.title('Численное интегрирование') 
#graph = Graph()
#ani = animation.FuncAnimation(f, Graphic, interval = 1000)
#graph.title('График сходимости методов')  
#graph.mainloop()
#app.bg("light-blue")
app.mainloop()

