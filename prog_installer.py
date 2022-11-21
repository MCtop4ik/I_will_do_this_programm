import tkinter
from tkinter import Label
from tkinter import Button
import os
#   import win10toast


def Phisic_Math_Programm():
    file_path = r'main.py'
    os.system("start " + file_path)

def chat_with_mods():
    file_path = r'client.py'
    os.system("start " + file_path)


window = tkinter.Tk()
window.title("Выберите приложение")
window.geometry('500x300')
window.resizable(width=False, height=True)

label_chos_prog = Label(

    window, text="Выбери приложение:",
    font=("Times New Roman", 33)

)
label_chos_prog.grid(

    column=0,
    row=0

           )

prog_btn = Button(

    window,
    text='Phisic&Math Programm',
    bg='blue',
    fg='#ccc',
    padx='80',
    pady='40',
    font='40',
    command=Phisic_Math_Programm

)

prog_btn_chat = Button(

    window,
    text='   Chat With Moderator   ',
    bg='#555',
    fg='#ccc',
    padx='80',
    pady='40',
    font='40',
    command=chat_with_mods

)

prog_btn_chat.grid(

    column=0,
    row=2

)

prog_btn.grid(

    column=0,
    row=1

)

window.mainloop()