import tkinter as tk
import json


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

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

    win.destroy()


def main_services(num):
    global win, breakfast, parking, add_bed, add_clean, chem_clean, teeth_kit, sew_kit, room_upgrade, ID

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

    # кнопка принятия данных

    tk.Button(win, text='Принять и завершить регистрацию',
              bd=2,
              command=accept_services, wraplength=150).grid(row=3, column=5, columnspan=2, rowspan=1, stick='wens')

    win.mainloop()


if __name__ == '__main__':
    main_services('1_1')
 