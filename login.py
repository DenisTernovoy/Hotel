import tkinter as tk


def check_guest():
    pass


def main_log():
    # конфигурация главного окна

    win_log = tk.Tk()

    win_log.title('Карточка клиента')
    win_log.geometry("600x400+400+150")
    win_log.columnconfigure(0, minsize=70)
    win_log.columnconfigure(1, minsize=70)
    win_log.columnconfigure(2, minsize=70)
    win_log.columnconfigure(3, minsize=70)
    win_log.columnconfigure(4, minsize=70)
    win_log.columnconfigure(5, minsize=70)
    win_log.columnconfigure(6, minsize=70)
    win_log.columnconfigure(7, minsize=70)

    win_log.rowconfigure(0, minsize=40)
    win_log.rowconfigure(1, minsize=40)
    win_log.rowconfigure(2, minsize=40)
    win_log.rowconfigure(3, minsize=40)
    win_log.rowconfigure(4, minsize=40)
    win_log.rowconfigure(5, minsize=40)

    win_log.resizable(False, False)

    tk.Label(win_log, text="Данные клиента",
             bg='#D0D5DE',
             font=("Arial", 20, 'bold')
             ).grid(row=0, column=0, columnspan=8, rowspan=2, stick='wens')

    # данные пользователя

    tk.Label(win_log, text="Серия паспорта:").grid(row=3, column=1)
    series_passport = tk.Entry(win_log, width=8)
    series_passport.grid(row=3, column=2, stick='w', padx=12)

    tk.Label(win_log, text="Номер паспорта:").grid(row=4, column=1)
    numbers_passport = tk.Entry(win_log, width=12)
    numbers_passport.grid(row=4, column=2, stick='e', padx=11)

    # кнопки

    tk.Button(win_log, text='Найти', bd=3,
              command=check_guest).grid(row=5, column=1, columnspan=2, stick='we')

    win_log.mainloop()

if __name__ == '__main__':
    main_log()