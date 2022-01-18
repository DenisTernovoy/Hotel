import tkinter as tk
import json


def check_guest():
    global name, surname, lastname, no_guest, room, flag_series_passport, flag_numbers_passport, \
        wrong_series_passport, wrong_numbers_passport, breakfast

    flag_series_passport = False
    flag_numbers_passport = False

    try:
        name.grid_forget()
    except Exception:
        pass

    try:
        surname.grid_forget()
    except Exception:
        pass

    try:
        lastname.grid_forget()
    except Exception:
        pass

    try:
        room.grid_forget()
    except Exception:
        pass

    try:
        no_guest.grid_forget()
    except Exception:
        pass

    try:
        wrong_series_passport.grid_forget()
    except Exception:
        pass

    try:
        wrong_numbers_passport.grid_forget()
    except Exception:
        pass

    try:
        breakfast.grid_forget()
    except Exception:
        pass


    if series_passport.get():
        if series_passport.get().isdigit():
            flag_series_passport = True
        else:
            wrong_series_passport = tk.Label(win_log, text='*',
                                             foreground='red')
            wrong_series_passport.grid(row=3, column=3, stick='w')

    if numbers_passport.get():
        if numbers_passport.get().isdigit():
            flag_numbers_passport = True
        else:
            wrong_numbers_passport = tk.Label(win_log, text='*',
                                              foreground='red')
            wrong_numbers_passport.grid(row=4, column=3, stick='w')

        # конечная проверка данных

    if flag_series_passport and flag_numbers_passport:

        with open('data.json', 'r') as json_file:
            j_dict = json.load(json_file)

        series = series_passport.get()
        numbers = numbers_passport.get()

        flag = True
        for ID in j_dict['Guests']:
            if f'{series}_{numbers}' == ID:
                flag = False
                name = tk.Label(win_log, text=f"Имя: {j_dict['Guests'][ID]['Name']} ")
                name.grid(row=3, column=4, columnspan=2, stick='w')
                surname = tk.Label(win_log, text=f"Фамилия: {j_dict['Guests'][ID]['Surname']} ")
                surname.grid(row=4, column=4, columnspan=2, stick='w')
                lastname = tk.Label(win_log, text=f"Отчество: {j_dict['Guests'][ID]['Lastname']} ")
                lastname.grid(row=5, column=4, columnspan=2, stick='w')
                room = tk.Label(win_log, text=f"Номер: {j_dict['Guests'][ID]['Room']} ")
                room.grid(row=6, column=4, columnspan=2, stick='w')

                if j_dict['Guests'][ID]['Breakfast'] == 1:
                    breakfast = tk.Label(win_log, text="Завтраки: Включены")
                    breakfast.grid(row=7, column=4, columnspan=2, stick='w')
                else:
                    breakfast = tk.Label(win_log, text="Завтраки: Не включены")
                    breakfast.grid(row=7, column=4, columnspan=2, stick='w')

                break

        if flag:
            no_guest = tk.Label(win_log, text="Гость не найден!", foreground='red')
            no_guest.grid(row=3, column=4, rowspan=3, columnspan=3)


def main_log():
    global series_passport, numbers_passport, win_log

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
    win_log.rowconfigure(6, minsize=40)
    win_log.rowconfigure(7, minsize=40)

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