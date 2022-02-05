import time
import tkinter as tk
import json
from summary import main_summary
from changes import main_change
from bills import main_bills
from sharing import main_share


def temp(num):
    ID = num
    win_log.destroy()
    main_log(ID)


def guests(collection):
    guests_list = collection

    def win(num):
        ID = num
        win_log.destroy()
        temp_win.destroy()
        main_log(ID)

    temp_win = tk.Tk()
    temp_win.title('Гости')
    temp_win.geometry('320x280+750+350')

    temp_win.rowconfigure(0, minsize=70)
    temp_win.rowconfigure(1, minsize=70)
    temp_win.rowconfigure(2, minsize=70)
    temp_win.rowconfigure(3, minsize=70)

    temp_win.columnconfigure(0, minsize=80)
    temp_win.columnconfigure(1, minsize=80)
    temp_win.columnconfigure(2, minsize=80)
    temp_win.columnconfigure(3, minsize=80)

    temp_win.resizable(False, False)

    tk.Label(temp_win, text='Гости',
             bg='#D0D5DE',
             font=("Arial", 18, 'bold')).grid(row=0, column=0, columnspan=4, stick='wens')

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

    tk.Button(temp_win,
              text=f"{j_dict['Guests'][guests_list[0]]['Name']} {j_dict['Guests'][guests_list[0]]['Surname']}",
              bd=3,
              command=lambda: win(guests_list[0]))\
        .grid(row=1, column=0, columnspan=4, stick='wens')

    if len(guests_list) == 2:
        tk.Button(temp_win,
                  text=f"{j_dict['Guests'][guests_list[1]]['Name']} {j_dict['Guests'][guests_list[1]]['Surname']}",
                  bd=3,
                  command=lambda: win(guests_list[1])) \
            .grid(row=2, column=0, columnspan=4, stick='wens')

    temp_win.mainloop()


def changes(num):
    win_log.destroy()
    ID = num
    main_change(ID)


def bill(num):
    ID = num
    main_bills(ID)


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

                find['state'] = tk.DISABLED
                flag = False

                name = tk.Label(win_log, text=f"Имя: {j_dict['Guests'][ID]['Name']} ")
                name.grid(row=3, column=4, columnspan=2, stick='w')

                surname = tk.Label(win_log, text=f"Фамилия: {j_dict['Guests'][ID]['Surname']} ")
                surname.grid(row=4, column=4, columnspan=2, stick='w')

                lastname = tk.Label(win_log, text=f"Отчество: {j_dict['Guests'][ID]['Lastname']} ")
                lastname.grid(row=5, column=4, columnspan=2, stick='w')

                room = tk.Label(win_log, text=f"Номер: {j_dict['Guests'][ID]['Room']['Number']} ")
                room.grid(row=6, column=4, columnspan=2, stick='w')

                date_arrival = tk.Label(win_log, text=f"Дата заезда: {j_dict['Guests'][ID]['Arrival']} ")
                date_arrival.grid(row=7, column=4, columnspan=2, stick='w')

                date_departure = tk.Label(win_log, text=f"Дата выезда: {j_dict['Guests'][ID]['Departure']['Date']} "
                                                        f"{j_dict['Guests'][ID]['Departure']['Time']}")
                date_departure.grid(row=8, column=4, columnspan=2, stick='w')

                if 'Share' in j_dict['Guests'][ID]:
                    tk.Button(win_log, text='Гость у', command=lambda: temp(j_dict['Guests'][ID]['Share']))\
                        .grid(row=9, column=4, columnspan=2, stick='wens')
                elif j_dict['Guests'][ID]['Share_with']:
                    tk.Button(win_log, text='Гости', command=lambda: guests(j_dict['Guests'][ID]['Share_with'])) \
                        .grid(row=9, column=4, columnspan=2, stick='wens')


                services = tk.Label(win_log, text="Услуги:",
                                    font=('Arial', 16, 'bold'))
                services.grid(row=9, column=1, columnspan=2, stick='w')

                count_row = 10
                count_сol = 1

                for i in j_dict['Guests'][ID]['Services']:
                    i = tk.Label(master=win_log, text=f"{i}: {j_dict['Guests'][ID]['Services'][i]} ")
                    i.grid(row=count_row, column=count_сol, columnspan=2, stick='w')
                    count_row += 1
                    if count_row == 16:
                        count_сol = 3
                        count_row = 10

                img = tk.PhotoImage(master=win_log, file=f'{series}_{numbers}.png')
                pers = tk.Label(win_log)
                pers.image = img
                pers['image'] = pers.image
                pers.grid(row=3, column=6, rowspan=10, columnspan=6, stick='w')

                total = tk.Label(win_log, text=f"Итого: {main_summary(f'{series}_{numbers}')} руб.",
                                    font=('Arial', 16, 'bold'))
                total.grid(row=17, column=1, columnspan=2, stick='w')

                if j_dict['Guests'][ID]['Alerts']:
                    tk.Label(win_log, text="Переезд:",
                             font=('Arial', 16, 'bold')).grid(row=18, column=1, columnspan=8, stick='w')
                    row = 19
                    for i in j_dict['Guests'][ID]['Alerts']:
                        tk.Label(win_log, text=f"{i}").grid(row=row, column=1, columnspan=8, stick='w')
                        row += 1

                change = tk.Button(win_log, text='Внести изменения', bd=3,
                                   command=lambda: changes(f'{series}_{numbers}'))
                change.grid(row=14, column=6, columnspan=5, stick='wens')

                bills = tk.Button(win_log, text='Чеки', bd=3,
                                   command=lambda: bill(f'{series}_{numbers}'))
                bills.grid(row=15, column=6, columnspan=5, stick='wens')

                share = tk.Button(win_log, text='Подселить гостя', bd=3,
                                  command=lambda: main_share(win_log, f'{series}_{numbers}'))
                share.grid(row=16, column=6, columnspan=5, stick='wens')

                if 'Share' in j_dict['Guests'][ID]:
                    share['state'] = tk.DISABLED
                break

        if flag:
            no_guest = tk.Label(win_log, text="Гость не найден!", foreground='red')
            no_guest.grid(row=3, column=4, rowspan=3, columnspan=3)


def main_log(data=None):
    global series_passport, numbers_passport, win_log, find

    # конфигурация главного окна

    win_log = tk.Tk()

    win_log.title('Карточка гостя')
    win_log.geometry("915x900+480+70")
    win_log.columnconfigure(0, minsize=80)
    win_log.columnconfigure(1, minsize=80)
    win_log.columnconfigure(2, minsize=80)
    win_log.columnconfigure(3, minsize=80)
    win_log.columnconfigure(4, minsize=80)
    win_log.columnconfigure(5, minsize=100)
    win_log.columnconfigure(6, minsize=80)
    win_log.columnconfigure(7, minsize=60)
    win_log.columnconfigure(8, minsize=60)
    win_log.columnconfigure(9, minsize=60)
    win_log.columnconfigure(10, minsize=60)
    win_log.columnconfigure(11, minsize=60)
    win_log.columnconfigure(12, minsize=60)
    win_log.columnconfigure(13, minsize=60)

    win_log.rowconfigure(0, minsize=40)
    win_log.rowconfigure(1, minsize=40)
    win_log.rowconfigure(2, minsize=40)
    win_log.rowconfigure(3, minsize=40)
    win_log.rowconfigure(4, minsize=40)
    win_log.rowconfigure(5, minsize=40)
    win_log.rowconfigure(6, minsize=40)
    win_log.rowconfigure(7, minsize=40)
    win_log.rowconfigure(8, minsize=40)
    win_log.rowconfigure(9, minsize=40)
    win_log.rowconfigure(10, minsize=40)
    win_log.rowconfigure(11, minsize=40)
    win_log.rowconfigure(12, minsize=40)
    win_log.rowconfigure(13, minsize=40)
    win_log.rowconfigure(14, minsize=40)
    win_log.rowconfigure(15, minsize=40)
    win_log.rowconfigure(16, minsize=40)
    win_log.rowconfigure(17, minsize=40)
    win_log.rowconfigure(18, minsize=40)
    win_log.rowconfigure(19, minsize=40)
    win_log.rowconfigure(20, minsize=40)
    win_log.rowconfigure(21, minsize=40)

    win_log.resizable(False, False)

    tk.Label(win_log, text="Данные гостя",
             bg='#D0D5DE',
             font=("Arial", 20, 'bold')
             ).grid(row=0, column=0, columnspan=12, rowspan=2, stick='wens')

    # данные пользователя

    tk.Label(win_log, text="Серия паспорта:").grid(row=3, column=1)
    series_passport = tk.Entry(win_log, width=8)
    series_passport.grid(row=3, column=2, stick='w', padx=12)

    tk.Label(win_log, text="Номер паспорта:").grid(row=4, column=1)
    numbers_passport = tk.Entry(win_log, width=12)
    numbers_passport.grid(row=4, column=2, stick='e', padx=11)

    # кнопки

    find = tk.Button(win_log, text='Найти', bd=3, command=check_guest)
    find.grid(row=5, column=1, columnspan=2, stick='we')

    if data:
        series_passport.insert(0, data.split('_')[0])
        numbers_passport.insert(0, data.split('_')[1])
        check_guest()

    win_log.mainloop()


if __name__ == '__main__':
    main_log('1_1')
