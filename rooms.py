import tkinter as tk
import json
from photo import main_photo


def choice_room(btn, room):
    btn['state'] = tk.DISABLED
    btn['bg'] = 'grey'

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

    j_dict['Guests'][ID]['Room']['Number'] = room
    j_dict['Guests'][ID]['Summary'] = {}
    j_dict['Guests'][ID]['Summary']['Number'] = 3000 * int(j_dict['Guests'][ID]['Stay'])

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

    win_r.destroy()
    main_photo(ID)


def check_room(room):
    room['state'] = tk.DISABLED
    room['bg'] = 'grey'


def main_win(a):
    global room_1, room_2, room_3, room_4, win_r, ID, DICT

    ID = a

    # конфигурация главного окна

    win_r = tk.Tk()
    win_r.geometry('350x400+500+200')
    win_r.title('Бронирование номера')

    win_r.columnconfigure(0, minsize=50)
    win_r.columnconfigure(1, minsize=50)
    win_r.columnconfigure(2, minsize=50)
    win_r.columnconfigure(3, minsize=50)
    win_r.columnconfigure(4, minsize=50)
    win_r.columnconfigure(5, minsize=50)
    win_r.columnconfigure(6, minsize=50)

    win_r.rowconfigure(0, minsize=50)
    win_r.rowconfigure(1, minsize=50)
    win_r.rowconfigure(2, minsize=50)
    win_r.rowconfigure(3, minsize=50)
    win_r.rowconfigure(4, minsize=50)
    win_r.rowconfigure(5, minsize=50)
    win_r.rowconfigure(6, minsize=50)
    win_r.resizable(False, False)
    win_r.overrideredirect(1)
    win_r.lift()
    win_r.attributes('-topmost', True)
    win_r.after_idle(win_r.attributes, '-topmost', True)

    # кнопки номеров

    room_1 = tk.Button(win_r, text='1', bg='green', bd=2, command=lambda: choice_room(room_1, 1))
    room_1.grid(row=1, column=1, padx=3, pady=3, stick='wens')
    room_2 = tk.Button(win_r, text='2', bg='green', bd=2, command=lambda: choice_room(room_2, 2))
    room_2.grid(row=1, column=2, padx=3, pady=3, stick='wens')
    room_3 = tk.Button(win_r, text='3', bg='green', bd=2, command=lambda: choice_room(room_3, 3))
    room_3.grid(row=1, column=3, padx=3, pady=3, stick='wens')
    room_4 = tk.Button(win_r, text='4', bg='green', bd=2, command=lambda: choice_room(room_4, 4))
    room_4.grid(row=1, column=4, padx=3, pady=3, stick='wens')
    room_5 = tk.Button(win_r, text='5', bg='green', bd=2, command=lambda: choice_room(room_5, 5))
    room_5.grid(row=1, column=5, padx=3, pady=3, stick='wens')
    room_6 = tk.Button(win_r, text='6', bg='green', bd=2, command=lambda: choice_room(room_6, 6))
    room_6.grid(row=2, column=1, padx=3, pady=3, stick='wens')
    room_7 = tk.Button(win_r, text='7', bg='green', bd=2, command=lambda: choice_room(room_7, 7))
    room_7.grid(row=2, column=2, padx=3, pady=3, stick='wens')
    room_8 = tk.Button(win_r, text='8', bg='green', bd=2, command=lambda: choice_room(room_8, 8))
    room_8.grid(row=2, column=3, padx=3, pady=3, stick='wens')
    room_9 = tk.Button(win_r, text='9', bg='green', bd=2, command=lambda: choice_room(room_9, 9))
    room_9.grid(row=2, column=4, padx=3, pady=3, stick='wens')
    room_10 = tk.Button(win_r, text='10', bg='green', bd=2, command=lambda: choice_room(room_10, 10))
    room_10.grid(row=2, column=5, padx=3, pady=3, stick='wens')
    room_11 = tk.Button(win_r, text='11', bg='green', bd=2, command=lambda: choice_room(room_11, 11))
    room_11.grid(row=3, column=1, padx=3, pady=3, stick='wens')
    room_12 = tk.Button(win_r, text='12', bg='green', bd=2, command=lambda: choice_room(room_12, 12))
    room_12.grid(row=3, column=2, padx=3, pady=3, stick='wens')
    room_13 = tk.Button(win_r, text='13', bg='green', bd=2, command=lambda: choice_room(room_13, 13))
    room_13.grid(row=3, column=3, padx=3, pady=3, stick='wens')
    room_14 = tk.Button(win_r, text='14', bg='green', bd=2, command=lambda: choice_room(room_14, 14))
    room_14.grid(row=3, column=4, padx=3, pady=3, stick='wens')
    room_15 = tk.Button(win_r, text='15', bg='green', bd=2, command=lambda: choice_room(room_15, 15))
    room_15.grid(row=3, column=5, padx=3, pady=3, stick='wens')
    room_16 = tk.Button(win_r, text='16', bg='green', bd=2, command=lambda: choice_room(room_16, 16))
    room_16.grid(row=4, column=1, padx=3, pady=3, stick='wens')
    room_17 = tk.Button(win_r, text='17', bg='green', bd=2, command=lambda: choice_room(room_17, 17))
    room_17.grid(row=4, column=2, padx=3, pady=3, stick='wens')
    room_18 = tk.Button(win_r, text='18', bg='green', bd=2, command=lambda: choice_room(room_18, 18))
    room_18.grid(row=4, column=3, padx=3, pady=3, stick='wens')
    room_19 = tk.Button(win_r, text='19', bg='green', bd=2, command=lambda: choice_room(room_19, 19))
    room_19.grid(row=4, column=4, padx=3, pady=3, stick='wens')
    room_20 = tk.Button(win_r, text='20', bg='green', bd=2, command=lambda: choice_room(room_20, 20))
    room_20.grid(row=4, column=5, padx=3, pady=3, stick='wens')
    room_21 = tk.Button(win_r, text='21', bg='green', bd=2, command=lambda: choice_room(room_21, 21))
    room_21.grid(row=5, column=1, padx=3, pady=3, stick='wens')
    room_22 = tk.Button(win_r, text='22', bg='green', bd=2, command=lambda: choice_room(room_22, 22))
    room_22.grid(row=5, column=2, padx=3, pady=3, stick='wens')
    room_23 = tk.Button(win_r, text='23', bg='green', bd=2, command=lambda: choice_room(room_23, 23))
    room_23.grid(row=5, column=3, padx=3, pady=3, stick='wens')
    room_24 = tk.Button(win_r, text='24', bg='green', bd=2, command=lambda: choice_room(room_24, 24))
    room_24.grid(row=5, column=4, padx=3, pady=3, stick='wens')
    room_25 = tk.Button(win_r, text='25', bg='green', bd=2, command=lambda: choice_room(room_25, 25))
    room_25.grid(row=5, column=5, padx=3, pady=3, stick='wens')

    DICT = {
        '1': room_1,
        '2': room_2,
        '3': room_3,
        '4': room_4,
        '5': room_5,
        '6': room_6,
        '7': room_7,
        '8': room_8,
        '9': room_9,
        '10': room_10,
        '11': room_11,
        '12': room_12,
        '13': room_13,
        '14': room_14,
        '15': room_15,
        '16': room_16,
        '17': room_17,
        '18': room_18,
        '19': room_19,
        '20': room_20,
        '21': room_21,
        '22': room_22,
        '23': room_23,
        '24': room_24,
        '25': room_25,
    }

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

    for guest in j_dict['Guests']:
        if j_dict['Guests'][guest]['Room'].get("Number", None):
            try:
                check_room(DICT[str(j_dict['Guests'][guest]['Room']['Number'])])
            except Exception:
                pass

    for room in DICT:
        if room in j_dict['Room_repair']:
            DICT[room]['state'] = tk.DISABLED
            DICT[room]['bg'] = 'red'

    win_r.mainloop()


if __name__ == '__main__':
    main_win('1_1')
