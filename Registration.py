import tkinter as tk
from rooms import main_win
import json
import datetime as dt

count = 0


def accept_all():
    global wrong_name, wrong_surname, wrong_l_name, result, count, wrong_series_passport, \
        wrong_numbers_passport, wrong_stay_time, date_departure, delta_days

    flag_name = False
    flag_surname = False
    flag_l_name = False
    flag_series_passport = False
    flag_numbers_passport = False
    flag_stay_time = False

    # удаление уведомлений об ошибках ввода

    try:
        wrong_name.grid_forget()
    except Exception:
        pass

    try:
        wrong_surname.grid_forget()
    except Exception:
        pass

    try:
        wrong_l_name.grid_forget()
    except Exception:
        pass

    try:
        result.grid_forget()
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
        wrong_stay_time.grid_forget()
    except Exception:
        pass

    # проверка ввода данных в каждый участок

    if name.get():
        if name.get().isalpha():
            flag_name = True
        else:
            wrong_name = tk.Label(win, text='*',
                                  foreground='red')
            wrong_name.grid(row=3, column=2, columnspan=2, stick='w')

    if surname.get():
        if surname.get().isalpha():
            flag_surname = True
        else:
            wrong_surname = tk.Label(win, text='*',
                                     foreground='red')
            wrong_surname.grid(row=4, column=2, columnspan=2, stick='w')

    if l_name.get():
        if l_name.get().isalpha():
            flag_l_name = True
        else:
            wrong_l_name = tk.Label(win, text='*',
                                    foreground='red')
            wrong_l_name.grid(row=5, column=2, columnspan=2, stick='w')

    if series_passport.get():
        if series_passport.get().isdigit():
            flag_series_passport = True
        else:
            wrong_series_passport = tk.Label(win, text='*',
                                             foreground='red')
            wrong_series_passport.grid(row=3, column=4, stick='e')

    if numbers_passport.get():
        if numbers_passport.get().isdigit():
            flag_numbers_passport = True
        else:
            wrong_numbers_passport = tk.Label(win, text='*',
                                              foreground='red')
            wrong_numbers_passport.grid(row=4, column=4, stick='e')

    if stay_time.get():
        arrange = stay_time.get().split('.')

        if [len(i) for i in arrange if i.isdigit()] == [2, 2, 4]:
            try:
                date_departure = dt.date(year=int(arrange[2]), month=int(arrange[1]), day=int(arrange[0]))
            except ValueError:
                wrong_stay_time = tk.Label(win, text='*',
                                           foreground='red')
                wrong_stay_time.grid(row=5, column=4, stick='e')
            else:
                delta_days = date_departure - dt.date.today()

                if delta_days.days < 0:
                    wrong_stay_time = tk.Label(win, text='*',
                                               foreground='red')
                    wrong_stay_time.grid(row=5, column=4, stick='e')
                elif delta_days.days == 0 and dt.datetime.now().time() > dt.time(5, 00, 00):
                    wrong_stay_time = tk.Label(win, text='*',
                                               foreground='red')
                    wrong_stay_time.grid(row=5, column=4, stick='e')
                else:
                    flag_stay_time = True
        else:
            wrong_stay_time = tk.Label(win, text='*',
                                              foreground='red')
            wrong_stay_time.grid(row=5, column=4, stick='e')

    # конечная проверка данных

    if flag_name and flag_surname and flag_l_name and flag_series_passport and flag_numbers_passport and flag_stay_time:

        with open('data.json', 'r') as json_file:
            j_dict = json.load(json_file)

        if f'{series_passport.get()}_{numbers_passport.get()}' in j_dict['Guests']:
            result = tk.Label(win, text='Гость уже зарегестрирован!',
                              foreground='black',
                              bg='red')
            result.grid(row=2, column=0, columnspan=6, stick='wens')
        else:
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}'] = dict()
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Name'] = name.get().capitalize()
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}'][
                'Surname'] = surname.get().capitalize()
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}'][
                'Lastname'] = l_name.get().capitalize()
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Room'] = {}
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Arrival'] = \
                f'{dt.datetime.today().strftime("%d.%m.%Y %H:%M")}'
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Departure'] = {}
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Departure']['Date'] = \
                f'{date_departure.strftime("%d.%m.%Y")}'
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Departure']['Time'] = '12:00'
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Stay'] = f'{delta_days.days}'
            j_dict['Guests'][f'{series_passport.get()}_{numbers_passport.get()}']['Alerts'] = []

            with open('data.json', 'w') as json_file:
                json.dump(j_dict, json_file, indent=4)

            result = tk.Label(win, text='Успешная регистрация!',
                              foreground='black',
                              bg='green')
            result.grid(row=2, column=0, columnspan=6, stick='wens')

            main_win(f'{series_passport.get()}_{numbers_passport.get()}')


def delete_all():
    name.delete(0, tk.END)
    surname.delete(0, tk.END)
    l_name.delete(0, tk.END)
    series_passport.delete(0, tk.END)
    numbers_passport.delete(0, tk.END)
    stay_time.delete(0, tk.END)

    try:
        result.grid_forget()
    except Exception:
        pass


def log_in():
    main_log()


def main():
    global win, name, surname, l_name, series_passport, numbers_passport, stay_time
    # конфигурация главного окна

    win = tk.Tk()
    win.title('Отель Гранд')
    win.geometry("600x400+400+150")

    win.columnconfigure(0, minsize=100)
    win.columnconfigure(1, minsize=100)
    win.columnconfigure(2, minsize=100)
    win.columnconfigure(3, minsize=100)
    win.columnconfigure(4, minsize=100)
    win.columnconfigure(5, minsize=100)
    win.columnconfigure(6, minsize=100)
    win.columnconfigure(7, minsize=100)

    win.rowconfigure(0, minsize=40)
    win.rowconfigure(1, minsize=40)
    win.rowconfigure(2, minsize=40)
    win.rowconfigure(3, minsize=40)
    win.rowconfigure(4, minsize=40)
    win.rowconfigure(5, minsize=40)
    win.rowconfigure(6, minsize=40)
    win.rowconfigure(7, minsize=40)

    tk.Label(win, text="Отель Гранд",
             bg='#D0D5DE',
             font=("Arial", 20, 'bold')
             ).grid(row=0, column=0, columnspan=6, rowspan=2, stick='wens')

    win.resizable(False, False)

    # данные пользователя

    tk.Label(win, text="Имя:").grid(row=3, column=0)
    name = tk.Entry(win)
    name.grid(row=3, column=1)

    tk.Label(win, text="Фамилия:").grid(row=4, column=0)
    surname = tk.Entry(win)
    surname.grid(row=4, column=1)

    tk.Label(win, text="Отчество:").grid(row=5, column=0)
    l_name = tk.Entry(win)
    l_name.grid(row=5, column=1)

    tk.Label(win, text="Серия паспорта:").grid(row=3, column=3)
    series_passport = tk.Entry(win, width=8)
    series_passport.grid(row=3, column=4, stick='w', padx=12)

    tk.Label(win, text="Номер паспорта:").grid(row=4, column=3, stick='e')
    numbers_passport = tk.Entry(win, width=12)
    numbers_passport.grid(row=4, column=4)

    tk.Label(win, text="Дата выезда:").grid(row=5, column=3)
    stay_time = tk.Entry(win, width=12)
    stay_time.grid(row=5, column=4)


    # кнопки передачи данных

    tk.Button(win, text='Принять',
              command=accept_all, bd=3).grid(row=6, column=0, stick='e')

    tk.Button(win, text='Очистить',
              command=delete_all, bd=3).grid(row=6, column=1, pady=20)

    win.mainloop()


if __name__=='__main__':
    main()