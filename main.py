from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import math
from math import *
from tkinter.ttk import Combobox
import sympy as sy
import time
import os
import random
import pyglet
#   from threading import Thread
import datetime
import win10toast
from PIL import Image, ImageTk
import cv2
from tkinter.ttk import Progressbar

#   2483313382402348964

root = Tk()
root.title("Physic&Math Programm")

print(os.environ)

#   root.geometry("1350x640")
root.geometry("325x230")

global sen
sen = 0
global new_window_1

new_window_1 = Toplevel(root)


def step():
    for i in range(20):
        new_window_1.update_idletasks()
        pb['value'] += 5
        time.sleep(1)
        txt['text'] = pb['value'], '%'


def progress():
    panel.destroy()
    global pb
    global txt
    root.geometry('700x150')
    label1123324432 = Label(text='Phisics&Math Community with MCtop4ik\n presents', font=("Times New Roman", 20))
    label1123324432.pack(side="top", fill="both", expand="yes")
    pb = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    pb.pack(side="bottom", fill="both", expand="yes")
    txt = Label(root, text='0%', bg='#345', fg='#fff')
    txt.pack(side="right", fill="both", expand="yes")
    for i in range(100):
        new_window_1.update_idletasks()
        pb['value'] += 1
        time.sleep(0.2)
        txt['text'] = pb['value'], '%'
    pb.destroy()
    txt.destroy()
    label1123324432.destroy()


def start_window_1():
    new_window_1.title("Авторизация")
    global label_login
    label_login = Label(new_window_1, text="Login")
    label_login.pack()
    global entry_login
    entry_login = Entry(new_window_1, width=10)
    entry_login.pack()
    global entry_pass
    global lbl_welcome
    global button1111
    global label_pass
    label_pass = Label(new_window_1, text="Password")
    label_pass.pack()
    entry_pass = Entry(new_window_1, width=16, show='*')
    entry_pass.pack()
    button1111 = Button(new_window_1, text="Enter", command=clicked)
    button1111.pack()
    global label_welcome
    lbl_welcome = Label(new_window_1)
    lbl_welcome.pack()


def clicked():
    if entry_login.get() and entry_pass.get():
        if entry_login.get() == 'andrej' and entry_pass.get() == '111111' or entry_login.get() == 'user' and entry_pass.get() == read_symbol():
            lbl_welcome["text"] = "Загружaется.\nВсе права на данное приложение \nпока принадлежат Zakharov Arseniy"
            label_login.destroy()
            label_pass.destroy()
            entry_login.destroy()
            entry_pass.destroy()
            button1111.destroy()
            progress()
            menu()
            new_window_1.after(1, new_window_1.destroy)
        elif entry_login.get() == 'System32' and entry_pass.get() == 'System64':
            messagebox.showerror('Индификационный номер:', read_for_message())
        elif entry_login.get() == 'senya' and entry_pass.get() == '1':
            label_login["text"] = " "
            label_pass["text"] = " "
            entry_login.destroy()
            entry_pass.destroy()
            button1111.destroy()
            panel.destroy()
            global sen
            sen = 0
            sen += 1
            menu()
            music()
        else:
            print("Incorect password or login")
            back()
    else:
        lbl_welcome.configure(text="Please enter the login\nand the password.")


def test_isEmpty():
    if os.stat("hello.txt").st_size == 0:
        with open("hello.txt", "a") as file:
            file.write(parol_variations())


def parol_variations():
    global m
    m = random.randint(0, len(array_parol))
    us = str(m)
    return us


def read_symbol():
    test_isEmpty()
    f = open('hello.txt', 'r')
    n = int(f.read(3))
    ex = array_parol[n]
    return ex


def read_for_message():
    test_isEmpty()
    f = open('hello.txt', 'r')
    n = int(f.read(3))
    return n


def menu():
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu1 = Menu(mainmenu, tearoff=0)
    tl = Menu(mainmenu, tearoff=0)
    yr = Menu(mainmenu, tearoff=0)
    alg = Menu(mainmenu, tearoff=0)
    zada = Menu(mainmenu, tearoff=0)
    photos = Menu(mainmenu, tearoff=0)

    mainmenu.add_cascade(label='Главная', menu=filemenu)
    mainmenu.add_cascade(label='Графики функций', menu=filemenu1)
    mainmenu.add_cascade(label='Алгебра', menu=alg)
    mainmenu.add_cascade(label='Уравнения', menu=yr)
    mainmenu.add_cascade(label='Таблицы', menu=tl)
    mainmenu.add_cascade(label='Решение задач', menu=zada)
    if sen == 1:
        mainmenu.add_cascade(label="Фотки", menu=photos)

    #    #filemenu.add_command(label="Музыка", command=music)
    filemenu.add_command(label='Командная строка', command=command)
    filemenu.add_command(label='Промокод', command=promocode)
    filemenu.add_command(label="Балланс", command=bal)
    filemenu.add_command(label="Магазин", command=shop)
    filemenu.add_command(label="Выход", command=back)

    filemenu1.add_command(label='y=kx', command=kx)
    filemenu1.add_command(label='y=kx+b', command=line_graphic)
    filemenu1.add_command(label='y=sin(x)', command=vitle)

    alg.add_command(label='Калькулятор', command=calculator)
    alg.add_command(label='Сортировка Пузырьком', command=buble_sort)
    alg.add_command(label='Генератор рандомных чисел', command=gen_random)
    alg.add_command(label='Упрощение выражение', command=easy_solve)
    alg.add_command(label='Раскрыть скобки в выражении', command=easy_expand)

    yr.add_command(label='Полное квадратное уравнение', command=kvadro)
    yr.add_command(label='Уравнение с одной переменной', command=x_equation)
    yr.add_command(label='Система уравнений', command=x_y_equation)
    yr.add_command(label='Система уравнений с тремя неизвестнами', command=x_y_z_equation)

    tl.add_command(label='Таблица плотностей', command=table_ro)
    tl.add_command(label="Таблица единиц измерений", command=table_ed)
    tl.add_command(label="Таблица удельной теплопроводности вещества", command=table_c)
    tl.add_command(label='Таблица линейного и объемного расширения вещества', command=table_alpha)

    zada.add_command(label='Задачи на плотность', command=density)

    photos.add_command(label='1', command=photo)
    #    panel.destroy()
    root.geometry("325x450")
    lbl = Label(root, text="ВЫБЕРИ ФИЗИЧЕСКУЮ ВЕЛИЧИНУ\nчтобы узнать о ней\nБОЛЬШЕ", font=("Times New Roman", 12))
    lbl.place(x=30, y=0)

    lettersphys = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'g', 'h', 'I', 'j', 'L',
                   'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 'T', 't', 'U', 'V', 'W', 'x',
                   'α', 'β', 'ε', 'η', 'θ', 'λ', 'μ', 'ν', 'ρ', 'σ', 'τ', 'υ', 'Φ', 'φ']

    for i in range(7):
        for j in range(8):
            Button(root, text=lettersphys[i * 6 + j], padx='10', pady='10', command=A).place(x=5 + 40 * j, y=75 + 45 * i)

    btn_w = Button(root, text='ω', padx='10', pady='10')
    btn_w.place(x=120, y=390)

    btn_const = Button(root, text='const', padx='20', pady='10')
    btn_const.place(x=165, y=390)

    my_birthday()


#    if sen==1:
#        lbl["text"]=" "
#        root.geometry('313x320')
#        img = ImageTk.PhotoImage(Image.open("olya2.jpg"))
#        panel = Label(root, image=img)
#        panel.pack(side="bottom", fill="both", expand="yes")


def A():
    A_win = Toplevel(root)
    A_win.title("Theory about 'A'")
    A_win.geometry("350x200")
    label_for_A = Label(A_win, text="Работа(Дж): ")

    formula = Label(A_win, text="\nA=F*s\nA=N*t", font=("Times New Roman", 16))
    explanation = Label(A_win, text=",где A-механическая работа;                    "
                                    "\nF-сила приложенная к телу;\n                 "
                                    "s-перемещение тела в направление действия силы;"
                                    "\nN-мощность;                                  "
                                    "\nt-время за которое совершалась работа;       ")
    label_for_A.place(x=0, y=0)
    formula.place(x=10, y=20)
    explanation.place(x=0, y=100)


def a():
    a_win = Toplevel(root)
    a_win.title("Theory about 'a'")
    label_a = Label(a_win, text='a-ускорение свободного падения;\n a=g')
    label_a.place(x=0, y=0)


def c():
    c_win = Toplevel(root)
    c_win.title("Theory about 'c'")
    c_win.geometry('325x205')

    label_c = Label(c_win, text="c-удельная теплоемкость вещества(Дж/(кг*С)")
    label_formula = Label(c_win, text="c=Q/(m*Δt)\nc=C/m", font=('Times New Roman', 14))
    label_explanation = Label(c_win, text=',где Q-количество теплоты;\n'
                                          'm-масса тела;\n'
                                          'Δt-изменение температуры тела.\nТакже имеет физический смысл как t₂-t₁;\n'
                                          'C-теплоемкость')

    table_but = Button(c_win, text='Таблица удельной теплоемкости', command=table_c)

    label_c.place(x=0, y=0)
    label_formula.place(x=0, y=20)
    label_explanation.place(x=0, y=90)
    table_but.place(x=60, y=175)


def C():
    win_C = Toplevel(root)
    win_C.title("Theory about 'C'")
    win_C.geometry('325x145')

    label_c = Label(win_C, text="C-Теплоёмкость тела из однородного вещества(Дж/ºC)")
    label_formula = Label(win_C, text="C=Q/Δt\nC=c*m", font=('Times New Roman', 14))
    label_explanation = Label(win_C, text=',где Q-количество теплоты;\n'
                                          'm-масса тела;\n'
                                          'Δt-изменение температуры тела.\nТакже имеет физический смысл как t₂-t₁;\n'
                                          'c-удельная теплоемкость')

    label_c.place(x=0, y=0)
    label_formula.place(x=0, y=20)
    label_explanation.place(x=0, y=60)


def E():
    win_E = Toplevel(root)
    win_E.title("Theory about 'E'")
    win_E.geometry('325x200')

    label_c = Label(win_E, text="E-Энергия(Дж)", font=('Times New Roman', 14))
    label_formula = Label(
        win_E,
        text="Потенциальная Энергия:\nE=mgh\nКинетическая Энергия:\nE=mʋ²/2",
        font=('Times New Roman', 14))
    label_explanation = Label(win_E, text=',где h-перемещение тела;\n'
                                        'm-масса тела;\n'
                                        'ʋ-скорость;\n'
                                        'g-ускорение свободного падения')

    label_c.place(x=0, y=0)
    label_formula.place(x=0, y=25)
    label_explanation.place(x=0, y=115)


def shop():
    music1 = Toplevel(root)
    music1.title("Магазин")
    btn = Button(music1, text="", command=goods1)
    btn1 = Button(music1, text="", command=timelapse)
    btn2 = Button(music1, text="", command=swing)
    btn.grid(column=0, row=0)
    btn1.grid(column=1, row=0)
    btn2.grid(column=2, row=0)
    stop_btn = Button(music1, text="", command=play_sound)
    stop_btn1 = Button(music1, text="", command=play_sound1)
    stop_btn2 = Button(music1, text="", command=play_sound2)
    stop_btn.grid(column=0, row=1)
    stop_btn1.grid(column=1, row=1)
    stop_btn2.grid(column=2, row=1)


def banning():
    messagebox.showwarning('БАН МАШИНА', 'Вы забанены')


def goods1():
    with open("ball.txt", "a") as file:
        file.write('-10000')


def bal():
    f11111 = open('ball.txt', 'r')
    n11111111 = int(f11111.read(2 ** 10))
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Phisics&Maths",
                       "На вашем балансе %s монет" % (n11111111))


def my_birthday():
    today = datetime.datetime.today()
    if today.strftime("%m-%d") == '01-01':
        print("Happy Birthday Arseniy!")
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("Phisics&Maths",
                           "Сегодня день рождения у одного из создателей данного приложения, Захарова Арсения")


def promocode():
    pr = Toplevel(root)
    label_prom = Label(pr, text="Promocode")
    label_prom.pack()
    global prom
    prom = Entry(pr, width=16, show='#')
    prom.pack()
    get = Button(pr, text="Получить", command=tested)
    get.pack()
    labl = read_symbol_promocode()
    print(labl)


def tested():
    if prom.get() == "Happy, Birthday!":
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("Phisics&Maths",
                           "Промокод активирован")
        back()
    else:
        toaster1 = win10toast.ToastNotifier()
        toaster1.show_toast(
            "Phisics&Maths",
            "Неверный промокод")


def test_isEmpty():
    if os.stat("promocode.txt").st_size == 0:
        with open("promocode.txt", "a") as file:
            file.write("Birthday")


def read_symbol_promocode():
    test_isEmpty()
    f = open('promocode.txt', 'r')
    n = f.read(16)
    return n


def photo():
    file_path = r'olya.jpg'
    os.system("start " + file_path)


def cam_spam():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('alph.png', frame)
    cap.release()


def music():
    music1 = Toplevel(root)
    music1.title("Музычка")
    btn = Button(music1, text="Summer_In_The_City", command=summer_in_the_city)
    btn1 = Button(music1, text="Timelapse", command=timelapse)
    btn2 = Button(music1, text="Swing", command=swing)
    btn.grid(column=0, row=0)
    btn1.grid(column=1, row=0)
    btn2.grid(column=2, row=0)
    stop_btn = Button(music1, text="Windfall", command=play_sound)
    stop_btn1 = Button(music1, text="Longen_Light", command=play_sound1)
    stop_btn2 = Button(music1, text="Faidherbe_Square", command=play_sound2)
    stop_btn.grid(column=0, row=1)
    stop_btn1.grid(column=1, row=1)
    stop_btn2.grid(column=2, row=1)


def summer_in_the_city():
    sound = pyglet.resource.media('Joe_Cocker_-_Summer_In_The_City_48125094.mp3')
    sound.play()
    pyglet.app.run()


def swing():
    sound1 = pyglet.media.load('Swing.mp3', streaming=False)
    sound1.play()
    pyglet.app.run()


def timelapse():
    sound2 = pyglet.media.load(r'TimeLapse.mp3', streaming=False)
    sound2.play()
    pyglet.app.run()


def play_sound1():
    sound2 = pyglet.media.load(r'Dalnii_Svet.mp3', streaming=False)
    sound2.play()
    pyglet.app.run()


def play_sound():
    sound2 = pyglet.media.load(r'Windfall.mp3', streaming=False)
    sound2.play()
    pyglet.app.run()


def play_sound2():
    sound2 = pyglet.media.load(r'Faidherbe_Squere.mp3', streaming=False)
    sound2.play()
    pyglet.app.run()


def table_ro():
    pl = Toplevel(root)
    pl.title("Таблица плотностей")
    label_pl = Label(pl, text='Таблица плотностей')
    label_pl.grid(column=0, row=0)
    combo = Combobox(pl, width=35)
    combo['values'] = ("Вода=1000кг/м3", "Алюминий=2700кг/м3", "Cталь=7800кг/м3", "Железо(Fe)=7800кг/м3",
                       "Ртуть=13600кг/м3", "Масло=900кг/м3")
    combo.current(0)  # установите вариант по умолчанию
    combo.grid(column=0, row=1)


def table_ed():
    ed = Toplevel(root)
    ed.title("Таблица единиц измерений")
    label_ed = Label(ed, text='Таблица единиц измерения')
    label_ed.grid(column=0, row=0)
    combo = Combobox(ed, width=35)
    combo['values'] = (
        "Плотность=кг/м^3", "Площадь=м^2", "Объем=м^3", "Расстояние=м", "Время=сек", "Масса=гр", "Скорость=м/сек",
        "Сила=Н(Ньютон)", "Ускорение свободного падения=Н/кг или м/с^2",
        "Коэффициент жесткости=Н/м", "Коэффициент трения - безразмерная величина", "Давление=Па(Паскаль)",
        "Работа=Дж(Джоуль)",
        "Мощность=Вт(Ватт)", "Момент силы=Н*м(Ньютон-метр)", "Энергия=Дж(Джоуль)", "КПД=%")
    combo.current(0)  # установите вариант по умолчанию
    combo.grid(column=0, row=1)


def table_c():
    c_tabl = Toplevel(root)
    c_tabl.title("Таблица удельной теплоемкости вещества")
    label_th = Label(c_tabl, text='Таблица удельной теплоемкости твердых тел')
    label_th.grid(column=0, row=0)
    combo_th = Combobox(c_tabl, width=35)
    combo_th['values'] = ('Золото=130(Дж/кг*ͦС)', 'Свинец=140(Дж/кг*ͦС)', 'Олово=230(Дж/кг*ͦС)',
                          'Серебро=250(Дж/кг*ͦС)', 'Медь=400(Дж/кг*ͦС)', 'Цинк=400(Дж/кг*ͦС)', 'Латунь=400(Дж/кг*ͦС)',
                          'Железо=460(Дж/кг*ͦС)', 'Сталь=500(Дж/кг*ͦС)', 'Чугун=540(Дж/кг*ͦС)', 'Графит=750(Дж/кг*ͦС)',
                          'Стекло=840(Дж/кг*ͦС)', 'Кирпич=880(Дж/кг*ͦС)', 'Алюминий=920(Дж/кг*ͦС)',
                          'Лед=2100(Дж/кг*ͦС)',
                          'Дерево(дуб)=2400(Дж/кг*ͦС)')
    combo_th.current(0)  # установите вариант по умолчанию
    combo_th.grid(column=0, row=1)

    label_w = Label(c_tabl, text='Таблица удельной теплоемкости жидких тел')
    label_w.grid(column=0, row=2)
    combo_w = Combobox(c_tabl, width=35)
    combo_w['values'] = ('Ртуть=140(Дж/кг*ͦС)', 'Железо=830(Дж/кг*ͦС)', 'Алюминий=1080(Дж/кг*ͦС)',
                         'Масло подсолнечное=1700(Дж/кг*ͦС)', 'Керосин=2100(Дж/кг*ͦС)', 'Эфир=2350(Дж/кг*ͦС)',
                         'Спирт=2500(Дж/кг*ͦС)', 'Вода=4200(Дж/кг*ͦС)')
    combo_w.current(0)  # установите вариант по умолчанию
    combo_w.grid(column=0, row=3)

    label_g = Label(c_tabl, text='Таблица удельной теплоемкости газообразных тел')
    label_g.grid(column=0, row=4)
    combo_g = Combobox(c_tabl, width=35)
    combo_g['values'] = ('Углекислый газ=830(Дж/кг*ͦС)', 'Кислород=920(Дж/кг*ͦС)', 'Воздух=1000(Дж/кг*ͦС)',
                         'Водяной пар=2200(Дж/кг*ͦС)', 'Гелий=5210(Дж/кг*ͦС)', 'Водород=5200(Дж/кг*ͦС)')
    combo_g.current(0)  # установите вариант по умолчанию
    combo_g.grid(column=0, row=5)


def table_alpha():
    alpha = Toplevel(root)
    alpha.title("Таблица коэффициентов линейного расширения")
    label_alpha = Label(alpha, text="Таблица коэффициентов линейного расширения(α)")
    label_alpha.grid(column=0, row=0)
    combo = Combobox(alpha, width=35)
    combo['values'] = ('Железо=1,2*10⁻⁵ºC⁻¹', 'Латунь=1,9*10⁻⁵ºC⁻¹', 'Медь=1,7*10⁻⁵ºC⁻¹', 'Сталь=1,1*10⁻⁵ºC⁻¹',
                       'Стекло=0,9*10⁻⁵ºC⁻¹', 'Цинк=3,0*10⁻⁵ºC⁻¹')
    combo.current(0)  # установите вариант по умолчанию
    combo.grid(column=0, row=1)

    label_beta = Label(alpha, text="Таблица коэффициентов объемного расширения(β)")
    label_beta.grid(column=0, row=2)
    combo_v = Combobox(alpha, width=35)
    combo_v['values'] = ('Нефть=1,0*10⁻³ºC⁻¹', 'Ртуть=1,8*10⁻⁴ºC⁻¹')
    combo_v.current(0)  # установите вариант по умолчанию
    combo_v.grid(column=0, row=3)
    label_beta_alpha = Label(alpha, text='Запомните отношение: β=3α')
    label_beta_alpha.grid(column=0, row=4)


def back():
    root.title("Мое первое приложение")
    root.geometry("500x250")
    root.after(1, root.destroy)
    sys.exit


def del_label():
    label12356789.destroy()


def del_label1():
    label123567890.destroy()


def smena1(Equel22, Lpart22):
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    New = str(sy.expand(Equel22))
    if New[0] != '-':
        New1 = '+' + str(New)
    else:
        New1 = str(New)

    # шифровка
    # "-"="~"
    # "+"="&"
    # "**"="^"
    # "*"="@"
    # "/"="!"
    t1 = New1.replace("+", "~")
    a1 = t1.replace('-', '&')
    b1 = a1.replace("**", "^")
    c11 = b1.replace("*1", "@")
    c111 = c11.replace("*2", "@")
    c1111 = c111.replace("*3", "@")
    c11111 = c1111.replace("*4", "@")
    c111111 = c11111.replace("*5", "@")
    c1111111 = c111111.replace("*6", "@")
    c11111111 = c1111111.replace("*7", "@")
    c111111111 = c11111111.replace("*8", "@")
    c1111111111 = c111111111.replace("*9", "@")
    c1 = c1111111111.replace("*0", "@")
    d111 = c1.replace("/(", "!(")
    d1 = d111.replace("/", "!")
    h1 = d1.replace("~", "-")
    g1 = h1.replace('&', '+')
    e1 = g1.replace("^", "**")
    f1 = e1.replace("@", "/")
    y1 = f1.replace('!(', '/(')
    z1 = y1.replace("!", "*")
    Last = Lpart22 + z1
    print(Last)
    return (Last)


def smena2(Equel, Lpart):
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    New = str(sy.expand(Equel))
    if New[0] != '-':
        New1 = '+' + str(New)
    else:
        New1 = str(New)
    #    #шифровка
    # "-"="~"
    # "+"="&"
    # "**"="^"
    # "*"="@"
    # "/"="!"
    t1 = New1.replace("+", "~")
    a1 = t1.replace('-', '&')
    b1 = a1.replace("**", "^")
    c11 = b1.replace("*1", "@")
    c111 = c11.replace("*2", "@")
    c1111 = c111.replace("*3", "@")
    c11111 = c1111.replace("*4", "@")
    c111111 = c11111.replace("*5", "@")
    c1111111 = c111111.replace("*6", "@")
    c11111111 = c1111111.replace("*7", "@")
    c111111111 = c11111111.replace("*8", "@")
    c1111111111 = c111111111.replace("*9", "@")
    c1 = c1111111111.replace("*0", "@")
    d111 = c1.replace("/(", "!(")
    d1 = d111.replace("/", "!")
    h1 = d1.replace("~", "-")
    g1 = h1.replace('&', '+')
    e1 = g1.replace("^", "**")
    f1 = e1.replace("@", "/")
    y1 = f1.replace('!(', '/(')
    z1 = y1.replace("!", "*")
    Last = Lpart + z1
    print(Last)
    return (Last)


def line_yravnenii2(Lpart1, Equel1, Lpart44, Equel44, Lpart441, Equel441):
    #    #Lpart1, Equel1, Lpart44, Equel44
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    w1 = Lpart1.replace('a', 'x')
    u1 = w1.replace('b', 'x')
    q1 = u1.replace('c', 'x')
    v1 = q1.replace('^', '**')
    l1 = v1.replace('x', 'x')
    d111 = l1.replace(',', '.')
    Lpart = d111.replace('z', 'z')
    w11 = Equel1.replace('a', 'x')
    u11 = w11.replace('b', 'x')
    q11 = u11.replace('c', 'x')
    v11 = q11.replace('^', '**')
    l11 = v11.replace('x', 'x')
    d1111 = l11.replace(',', '.')
    Equel = d1111.replace('z', 'z')
    w12 = Lpart44.replace('a', 'y')
    u12 = w12.replace('b', 'y')
    q12 = u12.replace('c', 'y')
    v12 = q12.replace('^', '**')
    l12 = v12.replace('y', 'y')
    d1112 = l12.replace(',', '.')
    Lpart22 = d1112.replace('z', 'z')
    w112 = Equel44.replace('a', 'y')
    u112 = w112.replace('b', 'y')
    q112 = u112.replace('c', 'y')
    v112 = q112.replace('^', '**')
    l112 = v112.replace('y', 'y')
    d11112 = l112.replace(',', '.')
    Equel22 = d11112.replace('z', 'z')
    w121 = Lpart441.replace('a', 'z')
    u121 = w121.replace('b', 'z')
    q121 = u121.replace('c', 'z')
    v121 = q121.replace('^', '**')
    l121 = v121.replace('z', 'z')
    d11121 = l121.replace(',', '.')
    Lpart221 = d11121.replace('z', 'z')
    w11211 = Equel441.replace('a', 'z')
    u1121 = w11211.replace('b', 'z')
    q1121 = u1121.replace('c', 'z')
    v1121 = q1121.replace('^', '**')
    l1121 = v1121.replace('z', 'z')
    d111121 = l1121.replace(',', '.')
    Equel221 = d111121.replace('z', 'z')
    #    Lpart=str(sy.simplify(Lpart2))
    ok = str(sy.solve((smena2(Equel, Lpart), smena1(Equel22, Lpart22), smena(Equel221, Lpart221)), (x, y, z)))
    #    ok=str(sy.solve((x-y-0,x+y-4),(x,y)))
    ok1 = ok.replace('.', ',')
    yes = ok1.replace('FiniteSet', '')
    label2335 = Label(x_y_z_yrav, text='Ответ:')
    label2335.place(x=10, y=190)
    global label123567890
    label123567890 = Label(x_y_z_yrav, text=str(yes))
    label123567890.place(x=60, y=190)


def line_yravnenii1(Lpart1, Equel1, Lpart44, Equel44):
    #   Lpart1, Equel1, Lpart44, Equel44
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    w1 = Lpart1.replace('a', 'x')
    u1 = w1.replace('b', 'x')
    q1 = u1.replace('c', 'x')
    v1 = q1.replace('^', '**')
    l1 = v1.replace('x', 'x')
    d111 = l1.replace(',', '.')
    Lpart = d111.replace('z', 'x')
    w11 = Equel1.replace('a', 'x')
    u11 = w11.replace('b', 'x')
    q11 = u11.replace('c', 'x')
    v11 = q11.replace('^', '**')
    l11 = v11.replace('x', 'x')
    d1111 = l11.replace(',', '.')
    Equel = d1111.replace('z', 'x')
    w12 = Lpart44.replace('a', 'y')
    u12 = w12.replace('b', 'y')
    q12 = u12.replace('c', 'y')
    v12 = q12.replace('^', '**')
    l12 = v12.replace('y', 'y')
    d1112 = l12.replace(',', '.')
    Lpart22 = d1112.replace('z', 'y')
    w112 = Equel44.replace('a', 'y')
    u112 = w112.replace('b', 'y')
    q112 = u112.replace('c', 'y')
    v112 = q112.replace('^', '**')
    l112 = v112.replace('y', 'y')
    d11112 = l112.replace(',', '.')
    Equel22 = d11112.replace('z', 'x')
    #    Lpart=str(sy.simplify(Lpart2))
    ok = str(sy.solve((smena2(Equel, Lpart), smena1(Equel22, Lpart22)), (x, y)))
    #    ok=str(sy.solve((x-y-0,x+y-4),(x,y)))
    ok1 = ok.replace('.', ',')
    yes = ok1.replace('FiniteSet', '')
    label2335 = Label(x_y_yrav, text='Ответ:')
    label2335.place(x=10, y=170)
    global label123567890
    label123567890 = Label(x_y_yrav, text=str(yes))
    label123567890.place(x=60, y=170)


def smena(Equel, Lpart):
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    New = str(sy.expand(Equel))
    if New[0] != '-':
        New1 = '+' + str(New)
    else:
        New1 = str(New)
    #       шифровка
    # "-"="~"
    # "+"="&"
    # "**"="^"
    # "*"="@"
    # "/"="!"
    t1 = New1.replace("+", "~")
    a1 = t1.replace('-', '&')
    b1 = a1.replace("**", "^")
    c11 = b1.replace("*1", "@")
    c111 = c11.replace("*2", "@")
    c1111 = c111.replace("*3", "@")
    c11111 = c1111.replace("*4", "@")
    c111111 = c11111.replace("*5", "@")
    c1111111 = c111111.replace("*6", "@")
    c11111111 = c1111111.replace("*7", "@")
    c111111111 = c11111111.replace("*8", "@")
    c1111111111 = c111111111.replace("*9", "@")
    c1 = c1111111111.replace("*0", "@")
    d111 = c1.replace("/(", "!(")
    d1 = d111.replace("/", "!")
    h1 = d1.replace("~", "-")
    g1 = h1.replace('&', '+')
    e1 = g1.replace("^", "**")
    f1 = e1.replace("@", "/")
    y1 = f1.replace('!(', '/(')
    z1 = y1.replace("!", "*")
    Last = Lpart + z1
    print(Last)
    return (Last)


def line_yravnenii(Lpart1, Equel1):
    a = sy.Symbol('a')
    b = sy.Symbol('b')
    c = sy.Symbol('c')
    x = sy.Symbol('x')
    y = sy.Symbol('y')
    z = sy.Symbol('z')
    # print("Напишите левую часть уравнения:")
    # Lpart1=input()
    # print("Напишите правую часть:")
    # Equel1=input()
    w1 = Lpart1.replace('a', 'x')
    u1 = w1.replace('b', 'x')
    q1 = u1.replace('c', 'x')
    v1 = q1.replace('^', '**')
    l1 = v1.replace('y', 'x')
    d111 = l1.replace(',', '.')
    Lpart = d111.replace('z', 'x')
    w11 = Equel1.replace('a', 'x')
    u11 = w11.replace('b', 'x')
    q11 = u11.replace('c', 'x')
    v11 = q11.replace('^', '**')
    l11 = v11.replace('y', 'x')
    d1111 = l11.replace(',', '.')
    Equel = d1111.replace('z', 'x')
    #    Lpart=str(sy.simplify(Lpart2))
    ok = str(sy.solveset(smena(Equel, Lpart), x))
    ok1 = ok.replace('.', ',')
    yes = ok1.replace('FiniteSet', '')
    label2335 = Label(x_yrav, text='Ответ:')
    label2335.place(x=10, y=150)
    global label12356789
    label12356789 = Label(x_yrav, text=str(yes))
    label12356789.place(x=60, y=150)


def sinus(w, phi, A, dy):
    global sin
    sin = 0
    xy = []
    for x in range(1000):
        y = math.sin(x * w)
        xy.append(x + phi)
        xy.append(y * A + dy)
    sin = canvas.create_line(xy, fill='#f00')


def buble_sort():
    bu = Toplevel(root)
    bu.geometry("325x230")
    lb = Label(bu, text='Сортировка Пузырьком. Введите массив чисел через пробел')
    lb.place(x=0, y=0)
    txt = Entry(bu, width=10)
    txt.place(x=0, y=30)
    btn123 = Button(bu, text='Рассортировать', command=do_bubble_sort)
    btn123.place(x=0, y=50)


def do_bubble_sort(array):
    nu = len(array)
    unordered = True
    while unordered:
        unordered = False
        for j in range(nu - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                unordered = True
        nu -= 1


def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")


def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0", "end")
    output.insert("0.0", value)


def handler():
    """ Get the content of entries and passes result to the output area """
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Проверь ввел ли ты 3 числа")


def solver(a, b, c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = "Дискрименант равен: %s \n X1 равен: %s \n X2 равен: %s \n" % (D, x1, x2)
    elif D == 0:
        D = int(D)
        x = (-b) / (2 * a)
        text = "Дискрименант равен %s, поэтому \nодин корень:  \n X1 равен: %s " % (D, x)
    else:
        text = "Дискрименант равен: %s \n Это уравнение не имеет решения так как \n дискрименант отрицательный" % D
    return text


def x_equation():
    global x_yrav
    x_yrav = Toplevel(root)
    x_yrav.title("Equation with one")
    x_yrav.geometry('300x300')

    c_lab = Label(x_yrav, text="Введи уравнение")
    c_lab.place(x=10, y=10)
    entry_A = Entry(x_yrav)
    entry_A.place(x=10, y=30)
    label_w = Label(x_yrav, text='=')
    label_w.place(x=120, y=30)
    entry_w = Entry(x_yrav)
    entry_w.place(x=140, y=30)

    btn_calc = Button(x_yrav, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: line_yravnenii(str(entry_A.get()),
                                                             str(entry_w.get())))
    btn_calc.place(x=10, y=50)

    label_w2 = Label(x_yrav,
                     text='Внимание программа не умеет\n считывать скрытое умножение.\n 2x-неправильно;\n 2*x-правильно')
    label_w2.place(x=10, y=80)

    btn_clean = Button(x_yrav, text='Очистить ответ', command=del_label)
    btn_clean.place(x=120, y=50)


def x_y_equation():
    global x_y_yrav
    x_y_yrav = Toplevel(root)
    x_y_yrav.title("Equation with two")
    x_y_yrav.geometry('300x300')

    c_lab = Label(x_y_yrav, text="Введите уравнения")
    c_lab.place(x=10, y=10)
    entry_A = Entry(x_y_yrav)
    entry_A.place(x=10, y=30)
    label_w = Label(x_y_yrav, text='=')
    label_w.place(x=120, y=30)
    entry_w = Entry(x_y_yrav)
    entry_w.place(x=140, y=30)

    entry_A1 = Entry(x_y_yrav)
    entry_A1.place(x=10, y=50)
    label_w1 = Label(x_y_yrav, text='=')
    label_w1.place(x=120, y=50)
    entry_w1 = Entry(x_y_yrav)
    entry_w1.place(x=140, y=50)

    btn_calc1 = Button(x_y_yrav, text='Рассчитать')
    btn_calc1.bind('<Button-1>', lambda event: line_yravnenii1(str(entry_A.get()),
                                                               str(entry_w.get()),
                                                               str(entry_A1.get()),
                                                               str(entry_w1.get())))
    btn_calc1.place(x=10, y=70)

    label_w2 = Label(x_y_yrav,
                     text='Внимание программа не умеет\n считывать скрытое умножение.\n 2x-неправильно;\n 2*x-правильно')
    label_w2.place(x=10, y=110)

    btn_clean = Button(x_y_yrav, text='Очистить ответ', command=del_label1)
    btn_clean.place(x=120, y=70)


def x_y_z_equation():
    global x_y_z_yrav
    x_y_z_yrav = Toplevel(root)
    x_y_z_yrav.title("Equation with three")
    x_y_z_yrav.geometry('300x300')

    c_lab = Label(x_y_z_yrav, text="Введите уравнения")
    c_lab.place(x=10, y=10)
    entry_A = Entry(x_y_z_yrav)
    entry_A.place(x=10, y=30)
    label_w = Label(x_y_z_yrav, text='=')
    label_w.place(x=120, y=30)
    entry_w = Entry(x_y_z_yrav)
    entry_w.place(x=140, y=30)

    entry_A1 = Entry(x_y_z_yrav)
    entry_A1.place(x=10, y=50)
    label_w1 = Label(x_y_z_yrav, text='=')
    label_w1.place(x=120, y=50)
    entry_w1 = Entry(x_y_z_yrav)
    entry_w1.place(x=140, y=50)

    entry_A12 = Entry(x_y_z_yrav)
    entry_A12.place(x=10, y=70)
    label_w12 = Label(x_y_z_yrav, text='=')
    label_w12.place(x=120, y=70)
    entry_w12 = Entry(x_y_z_yrav)
    entry_w12.place(x=140, y=70)

    btn_calc1 = Button(x_y_z_yrav, text='Рассчитать')
    btn_calc1.bind('<Button-1>', lambda event: line_yravnenii2(str(entry_A.get()),
                                                               str(entry_w.get()),
                                                               str(entry_A1.get()),
                                                               str(entry_w1.get()),
                                                               str(entry_A12.get()),
                                                               str(entry_w12.get())))
    btn_calc1.place(x=10, y=90)

    label_w2 = Label(x_y_z_yrav,
                     text='Внимание программа не умеет\n считывать скрытое умножение.\n 2x-неправильно;\n 2*x-правильно')
    label_w2.place(x=10, y=130)

    btn_clean = Button(x_y_z_yrav, text='Очистить ответ', command=del_label1)
    btn_clean.place(x=120, y=90)


def easy_solve():
    global easy_sol
    easy_sol = Toplevel(root)
    easy_sol.title("Упрощение выражения")
    easy_sol.geometry('300x300')

    c_lab = Label(easy_sol, text="Введи выражение которое нужно упростить")
    c_lab.place(x=10, y=10)
    entry_ADS = Entry(easy_sol)
    entry_ADS.place(x=10, y=30)

    btn_calc = Button(easy_sol, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: easier(str(entry_ADS.get())))
    btn_calc.place(x=10, y=50)

    label_w2 = Label(easy_sol,
                     text='Внимание программа не умеет\n считывать скрытое умножение.\n 2x-неправильно;\n 2*x-правильно \n Также в десятичных дробях запятую надо заменять\n на точку\n Возведение в степень **')
    label_w2.place(x=10, y=80)

    btn_clean = Button(easy_sol, text='Очистить ответ', command=del_label)
    btn_clean.place(x=120, y=50)


def easier(entry_ADS):
    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m \
        = sy.symbols('q w e r t y u i o p a s d f g h j k l z x c v b n m')
    ok = sy.simplify(entry_ADS)
    label2335 = Label(easy_sol, text='Ответ:')
    label2335.place(x=10, y=190)
    global label12356789
    label12356789 = Label(easy_sol, text=str(ok))
    label12356789.place(x=60, y=190)
    print(ok)


def easy_expand():
    global easy_ins
    easy_ins = Toplevel(root)
    easy_ins.title("Разложение")
    easy_ins.geometry('300x300')

    c_lab = Label(easy_ins, text="Введи выражение которое нужно упростить")
    c_lab.place(x=10, y=10)
    entry_ADS = Entry(easy_ins)
    entry_ADS.place(x=10, y=30)

    btn_calc = Button(easy_ins, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: expanded(str(entry_ADS.get())))
    btn_calc.place(x=10, y=50)

    label_w2 = Label(easy_ins,
                     text='Внимание программа не умеет\n считывать скрытое умножение.\n 2x-неправильно;\n 2*x-правильно \n Также в десятичных дробях запятую надо заменять\n на точку\n Возведение в степень **')
    label_w2.place(x=10, y=80)

    btn_clean = Button(easy_ins, text='Очистить ответ', command=del_label)
    btn_clean.place(x=120, y=50)


def expanded(entry_ADS):
    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m = sy.symbols(
        'q w e r t y u i o p a s d f g h j k l z x c v b n m')
    ok = sy.expand(entry_ADS)
    label2335 = Label(easy_ins, text='Ответ:')
    label2335.place(x=10, y=190)
    global label12356789
    label12356789 = Label(easy_ins, text=str(ok))
    label12356789.place(x=60, y=190)
    print(ok)


def kvadro():
    kv = Toplevel(root)
    kv.title("Quadratic calculator")
    kv.resizable(width=False, height=False)
    frame = Frame(kv)
    frame.grid()
    global a
    a = Entry(frame, width=3)
    a.grid(row=1, column=1, padx=(10, 0))
    a_lab = Label(frame, text="x**2+").grid(row=1, column=2)
    global b
    b = Entry(frame, width=3)
    b.grid(row=1, column=3)
    b_lab = Label(frame, text="x+").grid(row=1, column=4)
    global c
    c = Entry(frame, width=3)
    c.grid(row=1, column=5)
    c_lab = Label(frame, text="= 0").grid(row=1, column=6)
    but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))
    global output
    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=2, columnspan=8)
    a.bind("<FocusIn>", clear)
    b.bind("<FocusIn>", clear)
    c.bind("<FocusIn>", clear)


def clean():
    canvas.delete(sin)


def density():
    plo = Toplevel(root)
    global chk_state
    global chk_state1
    global chk_state2
    global chk_state3
    global chk_state4
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    chk_state1 = BooleanVar()
    chk_state1.set(True)  # задайте проверку состояния чекбокса
    chk_state2 = BooleanVar()
    chk_state2.set(True)  # задайте проверку состояния чекбокса
    chk_state3 = BooleanVar()
    chk_state3.set(True)  # задайте проверку состояния чекбокса
    chk_state4 = BooleanVar()
    chk_state4.set(True)  # задайте проверку состояния чекбокса
    chk = Checkbutton(plo, text='Плотность', var=chk_state)
    chk.grid(column=0, row=0)
    chk1 = Checkbutton(plo, text='Объем', var=chk_state1)
    chk1.grid(column=1, row=0)
    chk2 = Checkbutton(plo, text='Масса', var=chk_state2)
    chk2.grid(column=2, row=0)
    chk3 = Checkbutton(plo, text='Высота', var=chk_state3)
    chk3.grid(column=0, row=1)
    chk4 = Checkbutton(plo, text='Площадь', var=chk_state4)
    chk4.grid(column=1, row=1)
    btn = Button(plo, text="Выбрать", command=test_checkbox)
    btn.grid(column=0, row=2)


def test_checkbox():
    if chk_state.get():
        idk = 1
        print('ok')
    if chk_state1.get():
        idk1 = 1
        print('ok')
    if chk_state2.get():
        idk2 = 1
        print('ok')
    if chk_state3.get():
        idk3 = 1
        print('ok')
    if chk_state4.get():
        idk4 = 1
        print('ok')


def line_func(x, k, b222):
    global l_f
    l_f = 0
    xy = []
    for i in range(1000):
        xy.append(x * i)
        xy.append((x * k + b222) * i)
    l_f = canvas.create_line(xy, fill='#f00')


def line_graphic():
    graf = Toplevel(root)
    graf.title("Построение графика функции y=kx+b")
    graf.geometry("1350x640")
    global canvas
    canvas = Canvas(graf, width=1040, height=640, bg='#002')
    for y in range(21):
        k = 50 * y
        canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill="#191930")

    for x in range(13):
        k = 50 * x
        canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill="#191930")

    canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='white')
    canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='white')
    canvas.create_text(20, 10, text='300', fill="white")
    canvas.create_text(20, 630, text='-300', fill="white")
    canvas.create_text(10, 310, text='0', fill="white")
    canvas.create_text(1020, 310, text='1000', fill="white")

    label_phi = Label(graf, text='Смещение графика по x: ')
    label_phi.place(x=0, y=10)
    #    label_dy = Label(graf, text='Смещение по y: ')
    #    label_dy.place(x=0, y=30)
    label_A = Label(graf, text='Угловой коэффициент: ')
    label_A.place(x=0, y=30)
    label_w = Label(graf, text='Пересечение с ОУ')
    label_w.place(x=0, y=50)

    entry_phi = Entry(graf)
    entry_phi.place(x=150, y=10)
    #    entry_dy = Entry(graf)
    #    entry_dy.place(x=150, y=30)
    entry_A = Entry(graf)
    entry_A.place(x=150, y=30)
    entry_w = Entry(graf)
    entry_w.place(x=150, y=50)

    btn_calc = Button(graf, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: line_func(float(entry_phi.get()),
                                                        float(entry_A.get()),
                                                        float(entry_w.get())))
    btn_calc.place(x=10, y=100)
    canvas.pack(side='right')


def kx_gr(k):
    global l_g
    l_g = 0
    xy = []
    for i in range(-100, 1000):
        xy.append(i)
        xy.append(i * k)
    l_g = canvas.create_line(xy, fill='#f00')
    print(xy)


def kx():
    graf = Toplevel(root)
    graf.title("Построение графика функции y=kx")
    graf.geometry("1350x640")
    global canvas
    canvas = Canvas(graf, width=1040, height=640, bg='#002')
    for y in range(21):
        k = 50 * y
        canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill="#191930")

    for x in range(13):
        k = 50 * x
        canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill="#191930")

    canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='white')
    canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='white')
    canvas.create_text(20, 10, text='300', fill="white")
    canvas.create_text(20, 630, text='-300', fill="white")
    canvas.create_text(10, 310, text='0', fill="white")
    canvas.create_text(1020, 310, text='1000', fill="white")

    label_A = Label(graf, text='Угловой коэффициент: ')
    label_A.place(x=0, y=10)

    entry_A = Entry(graf)
    entry_A.place(x=150, y=10)

    btn_calc = Button(graf, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: kx_gr(float(entry_A.get())))
    btn_calc.place(x=10, y=100)
    canvas.pack(side='right')


def vitle():
    graf = Toplevel(root)
    graf.title("Построение графика функции y=sin(x)")
    graf.geometry("1350x640")
    global canvas
    canvas = Canvas(graf, width=1040, height=640, bg='#002')
    for y in range(21):
        k = 50 * y
        canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill="#191930")

    for x in range(13):
        k = 50 * x
        canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill="#191930")

    canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='white')
    canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='white')
    canvas.create_text(20, 10, text='300', fill="white")
    canvas.create_text(20, 630, text='-300', fill="white")
    canvas.create_text(10, 310, text='0', fill="white")
    canvas.create_text(1020, 310, text='1000', fill="white")

    label_w = Label(graf, text='Циклическая частота: ')
    label_w.place(x=0, y=10)
    label_phi = Label(graf, text='Смещение графика по x: ')
    label_phi.place(x=0, y=30)
    label_A = Label(graf, text='Амплитуда: ')
    label_A.place(x=0, y=50)
    label_dy = Label(graf, text='Смещение по координате y: ')
    label_dy.place(x=0, y=70)

    entry_w = Entry(graf)
    entry_w.place(x=150, y=10)
    entry_phi = Entry(graf)
    entry_phi.place(x=150, y=30)
    entry_A = Entry(graf)
    entry_A.place(x=150, y=50)
    entry_dy = Entry(graf)
    entry_dy.place(x=150, y=70)

    btn_calc = Button(graf, text='Рассчитать')
    btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()),
                                                    float(entry_phi.get()),
                                                    float(entry_A.get()),
                                                    float(entry_dy.get())))
    btn_calc.place(x=10, y=100)
    #    btn_clean = Button(root, text='Очистить')
    # btn_clean.place(x=100, y=100)
    # btn_clean.bind(command=back)
    canvas.pack(side='right')


# def func():
# menu1 = Menu(root)
# new_item1 = Menu(menu1)
# new_item1.add_command(label='y=kx')
# new_item1.add_command(label='y=sin(x)', command=vitle)
# new_item1.add_command(label='Выйти',command=back)
# menu1.add_cascade(label='Графики функций', menu=new_item1)
# root.config(menu=menu1)


def calc(key):
    global memory
    if key == "=":
        # исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        # исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)


def command():
    file_path = r'C:\windows\system32\cmd.exe'
    os.system("start " + file_path)


def calculator():
    calcul = Toplevel(root)
    calcul.geometry("350x225")
    calcul.title("Калькулятор")
    global calc_entry
    calc_entry = Entry(calcul, width=33)
    bttn_list = [
        "7", "8", "9", "+", "*",
        "4", "5", "6", "-", "/",
        "1", "2", "3", "=", "xⁿ",
        "0", ".", "±", "C"
        , "π", "sin", "cos",
        "(", ")", "n!", "√2", ]
    r = 1
    c = 0
    for i in bttn_list:
        rel = ""
        cmd = lambda x=i: calc(x)
        ttk.Button(calcul, text=i, command=cmd, width=10).grid(row=r, column=c)
        c += 1
        if c > 4:
            c = 0
            r += 1
    calc_entry.grid(row=0, column=0, columnspan=5)


def pic():
    root.geometry('313x320')
    img = ImageTk.PhotoImage(Image.open("olya2.jpg"))
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")


def gen_random():
    rnd = Toplevel(root)
    rnd_a = Entry(rnd, width=10, state='disabled')
    rnd_b = Entry
    rnd_num = random.randint(rnd_a.get(), rnd_b.get())


global array_parol
array_parol = ["296038", '370609', '565637', '106111', '591690', '245624', '685061', '344545', '741246', '631208',
               '700100', '621259', '566447', '401354', '405118', '203106', '669478', '291536', '437232', '779244']

#   new_item.add_separator()
#   new_item.add_command(label='Сортировка', command=bubble_sort)
#   menu.add_cascade(label='Выбрать операцию', menu=new_item)


start_window_1()
global panel

#   root.geometry('313x320')
#   img = ImageTk.PhotoImage(Image.open("olya2.jpg"))
#   panel = Label(root, image=img)
#   panel.pack(side="bottom", fill="both", expand="yes")


root.geometry('500x500')

img = ImageTk.PhotoImage(Image.open("cat.png"))
panel = Label(root, image=img)

panel.pack(side="bottom", fill="both", expand="yes")

#   print(read_symbol())


root.mainloop()
