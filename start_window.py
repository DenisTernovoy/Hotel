import tkinter as tk
import json
from Registration import main
from login import main_log
from room_state import room_state_func


def root():
    # конфигурация главного окна

    root = tk.Tk()
    root.title('Отель Гранд')
    root.geometry('580x340+650+250')

    root.rowconfigure(0, minsize=40)
    root.rowconfigure(1, minsize=40)
    root.rowconfigure(2, minsize=40)
    root.rowconfigure(3, minsize=40)
    root.rowconfigure(4, minsize=40)
    root.rowconfigure(5, minsize=40)
    root.rowconfigure(6, minsize=40)
    root.rowconfigure(7, minsize=40)

    root.columnconfigure(0, minsize=145)
    root.columnconfigure(1, minsize=145)
    root.columnconfigure(2, minsize=145)
    root.columnconfigure(3, minsize=145)

    root.resizable(False, False)

    tk.Label(root, text='Главное меню',
             font=('Arial', 20, 'bold'), bg='#D0D5DE').grid(row=0, column=0, rowspan=2, columnspan=4, stick='wens')

    # основное меню

    tk.Button(root, text='Регистрация', command=main, bd=3, activebackground="white").\
        grid(row=2, column=0, rowspan=2, stick='wens')
    tk.Button(root, text='Карточка гостя', command=main_log, bd=3, activebackground="white").\
        grid(row=2, column=1, rowspan=2, stick='wens')
    tk.Button(root, text='Состояние комнат', command=room_state_func, bd=3, activebackground="white").\
        grid(row=2, column=2, rowspan=2, stick='wens')
    tk.Button(root, text='База гостей', command=main, bd=3, activebackground="white").\
        grid(row=2, column=3, rowspan=2, stick='wens')

    root.mainloop()


if __name__ == '__main__':
    root()