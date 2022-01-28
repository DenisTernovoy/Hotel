import tkinter as tk
import json
import time


def accept_services():

    with open("data.json", 'r') as json_file:
        j_dict = json.load(json_file)

        j_dict['Guests'][ID]['Services'] = {}
        j_dict['Guests'][ID]['Services']['Breakfast'] = breakfast.get()
        j_dict['Guests'][ID]['Services']['Parking'] = parking.get()
        j_dict['Guests'][ID]['Services']['Add_bed'] = add_bed.get()
        j_dict['Guests'][ID]['Services']['Add_clean'] = add_clean.get()
        j_dict['Guests'][ID]['Services']['Chem_clean'] = chem_clean.get()
        j_dict['Guests'][ID]['Services']['Teeth_kit'] = teeth_kit.get()
        j_dict['Guests'][ID]['Services']['Sew_kit'] = sew_kit.get()
        j_dict['Guests'][ID]['Services']['Room_upgrade'] = room_upgrade.get()
        j_dict['Guests'][ID]['Services']['Early_arrival'] = early_arrival.get()
        j_dict['Guests'][ID]['Services']['Late_departure'] = late_departure.get()
        j_dict['Guests'][ID]['Services']['Night_arrival'] = night_arrival.get()

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

    def temp_accept(name):
        option = name

        def temp_accept_2(name):
            global wrong_day, wrong_num
            option = name
            flag_breakfast = False
            flag_person = False

            try:
                wrong_day.grid_forget()
            except Exception:
                pass

            try:
                wrong_num.grid_forget()
            except Exception:
                pass

            try:
                int(day_temp.get())
            except Exception:
                wrong_day = tk.Label(temp, text='*',
                                     foreground='red')
                wrong_day.grid(row=1, column=3, stick='e')
            else:
                flag_person = True

            try:
                int(breakfast_temp.get())
            except Exception:
                wrong_num = tk.Label(temp, text='*',
                                     foreground='red')
                wrong_num.grid(row=0, column=3, stick='e')
            else:
                flag_breakfast = True

            if flag_person and flag_breakfast:

                with open("data.json", 'r') as json_file:
                    j_dict = json.load(json_file)

                if (j_dict['Guests'][ID]['Services']['Early_arrival'] == 1 or
                    j_dict['Guests'][ID]['Services']['Night_arrival'] == 1) and \
                        int(day_temp.get()) > int(j_dict['Guests'][ID]['Stay']) + 1:
                    wrong_day = tk.Label(temp, text='*',
                                         foreground='red')
                    wrong_day.grid(row=1, column=3, stick='e')
                elif int(day_temp.get()) > int(j_dict['Guests'][ID]['Stay']) and \
                        (j_dict['Guests'][ID]['Services']['Early_arrival'] == 0 and
                         j_dict['Guests'][ID]['Services']['Night_arrival'] == 0):
                    wrong_day = tk.Label(temp, text='*',
                                         foreground='red')
                    wrong_day.grid(row=1, column=3, stick='e')

                else:
                    j_dict['Guests'][ID]['Summary'][f'{option}'] = int(day_temp.get()) * int(
                        breakfast_temp.get()) * 1000
                    j_dict['Guests'][ID]['Services'][f'{option}'] = f'{breakfast_temp.get()} ч. x {day_temp.get()} д.'

                    with open('data.json', 'w') as json_file:
                        json.dump(j_dict, json_file, indent=4)

                    temp.destroy()
                    return

        temp = tk.Tk()
        temp.geometry('240x120+750+350')
        temp.title(f'{option.capitalize()}')
        temp.rowconfigure(0, minsize=40)
        temp.rowconfigure(1, minsize=40)
        temp.rowconfigure(2, minsize=40)

        temp.columnconfigure(0, minsize=60)
        temp.columnconfigure(1, minsize=60)
        temp.columnconfigure(2, minsize=60)
        temp.columnconfigure(3, minsize=60)

        tk.Label(temp, text='Количество персон:').grid(row=0, column=0, columnspan=2)
        breakfast_temp = tk.Entry(temp, width=5)
        breakfast_temp.grid(row=0, column=2)

        tk.Label(temp, text='Количество дней:').grid(row=1, column=0, columnspan=2)
        day_temp = tk.Entry(temp, width=5)
        day_temp.grid(row=1, column=2)

        tk.Button(temp, text='OK', command=lambda:temp_accept_2(option)).grid(row=0, column=3, columnspan=2, rowspan=2)

    if breakfast.get() == 1:
        temp_accept('Breakfast')
    if parking.get() == 1:
        temp_accept('Parking')
    if late_departure.get() == 1:

        with open("data.json", 'r') as json_file:
            j_dict = json.load(json_file)

        j_dict['Guests'][ID]['Departure']['Time'] = "18:00"

        with open('data.json', 'w') as json_file:
            json.dump(j_dict, json_file, indent=4)

    win.destroy()


def main_services(num):
    global win, breakfast, parking, add_bed, add_clean, chem_clean, teeth_kit, sew_kit, room_upgrade, early_arrival,\
        late_departure, night_arrival, ID

    ID = num
    # настройка главного окна

    win = tk.Tk()
    win.title('Дополнительные услуги')
    win.geometry("480x480+450+150")

    win.columnconfigure(0, minsize=60)
    win.columnconfigure(1, minsize=60)
    win.columnconfigure(2, minsize=60)
    win.columnconfigure(3, minsize=60)
    win.columnconfigure(4, minsize=60)
    win.columnconfigure(5, minsize=60)
    win.columnconfigure(6, minsize=60)
    win.columnconfigure(7, minsize=60)

    win.rowconfigure(0, minsize=50)
    win.rowconfigure(1, minsize=50)
    win.rowconfigure(2, minsize=50)
    win.rowconfigure(3, minsize=50)
    win.rowconfigure(4, minsize=50)
    win.rowconfigure(5, minsize=50)
    win.rowconfigure(6, minsize=50)
    win.rowconfigure(7, minsize=50)
    win.rowconfigure(8, minsize=50)

    win.resizable(False, False)

    tk.Label(win, text="Каталог услуг",
             bg='#D0D5DE',
             font=("Arial", 18, 'bold')
             ).grid(row=0, column=0, columnspan=8, stick='wens')

    # кнопки - флаги

    breakfast = tk.IntVar(win)
    tk.Checkbutton(win, text='Завтраки', variable=breakfast).grid(row=2, column=1, columnspan=2, stick='w')

    parking = tk.IntVar(win)
    tk.Checkbutton(win, text='Парковка', variable=parking).grid(row=3, column=1, columnspan=2, stick='w')

    add_bed = tk.IntVar(win)
    tk.Checkbutton(win, text='Доп. кровать', variable=add_bed).grid(row=4, column=1, columnspan=2, stick='w')

    add_clean = tk.IntVar(win)
    tk.Checkbutton(win, text='Доп. уборка', variable=add_clean).grid(row=5, column=1, columnspan=2, stick='w')

    chem_clean = tk.IntVar(win)
    tk.Checkbutton(win, text='Химчистка', variable=chem_clean).grid(row=6, column=1, columnspan=2, stick='w')

    teeth_kit = tk.IntVar(win)
    tk.Checkbutton(win, text='Зубные наборы', variable=teeth_kit).grid(row=7, column=1, columnspan=2, stick='w')

    sew_kit = tk.IntVar(win)
    tk.Checkbutton(win, text='Швейные наборы', variable=sew_kit).grid(row=8, column=1, columnspan=2, stick='w')

    room_upgrade = tk.IntVar(win)
    tk.Checkbutton(win, text='Апгрейд номера', variable=room_upgrade).grid(row=2, column=5, columnspan=2, stick='w')

    early_arrival = tk.IntVar(win)
    tk.Checkbutton(win, text='Ранний заезд', variable=early_arrival).grid(row=3, column=5, columnspan=2, stick='w')

    late_departure = tk.IntVar(win)
    tk.Checkbutton(win, text='Поздний выезд', variable=late_departure).grid(row=4, column=5, columnspan=2, stick='w')

    night_arrival = tk.IntVar(win)
    tk.Checkbutton(win, text='Ночной заезд', variable=night_arrival).grid(row=5, column=5, columnspan=2, stick='w')

    # кнопка принятия данных

    tk.Button(win, text='Принять и завершить регистрацию',
              bd=2,
              command=accept_services, wraplength=150).grid(row=7, column=5, columnspan=2, rowspan=1, stick='wens')

    win.mainloop()


if __name__ == '__main__':
    main_services('1_1')
 