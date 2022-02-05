import tkinter as tk
import json
from login import main_log


def finish(num):
    room = num

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

        del j_dict["Room_repair"][room]

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

    temp.destroy()
    state.destroy()


def choice_room(room):
    global temp
    state.destroy()

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

        if str(room) in j_dict["Room_repair"]:
            temp = tk.Tk()
            temp.geometry('420x320+750+300')
            temp.title('Состояние комнаты')

            temp.rowconfigure(0, minsize=40)
            temp.rowconfigure(1, minsize=40)
            temp.rowconfigure(2, minsize=40)
            temp.rowconfigure(3, minsize=40)
            temp.rowconfigure(4, minsize=40)
            temp.rowconfigure(5, minsize=40)
            temp.rowconfigure(6, minsize=40)

            temp.columnconfigure(0, minsize=60)
            temp.columnconfigure(1, minsize=60)
            temp.columnconfigure(2, minsize=60)
            temp.columnconfigure(3, minsize=60)
            temp.columnconfigure(4, minsize=60)
            temp.columnconfigure(5, minsize=60)
            temp.columnconfigure(6, minsize=60)

            temp.resizable(False, False)

            tk.Label(temp, text=f'Состояние номера: {room}',
                     font=('Arial', 20, 'bold'), bg='#D0D5DE').grid(row=0, column=0, rowspan=2, columnspan=7,
                                                                    stick='wens')
            row = 2
            for i in j_dict["Room_repair"][str(room)]:
                tk.Label(temp, text=f'\t{row - 1}) {i}').grid(row=row, column=0, rowspan=2, columnspan=7,
                                                                    stick='w')
                row += 1

            tk.Button(temp, text='Исправлено', command=lambda: finish(str(room))).\
                grid(row=6, column=1, columnspan=2, stick='wens')

            tk.Button(temp, text='Закрыть', command=lambda: temp.destroy()).\
                grid(row=6, column=4, columnspan=2, stick='wens')

            temp.mainloop()

        else:
            for guest in j_dict["Guests"]:
                try:
                    str(j_dict["Guests"][guest]["Room"]["Number"])
                except Exception:
                    pass
                else:
                    if str(room) == str(j_dict["Guests"][guest]["Room"]["Number"]):
                        main_log(guest)
                        break


def room_state_func():
    global state, DICT, room_repair

    # конфигурация главного окна

    state = tk.Tk()
    state.geometry('350x400+500+200')
    state.title('Состояние номеров')

    state.columnconfigure(0, minsize=50)
    state.columnconfigure(1, minsize=50)
    state.columnconfigure(2, minsize=50)
    state.columnconfigure(3, minsize=50)
    state.columnconfigure(4, minsize=50)
    state.columnconfigure(5, minsize=50)
    state.columnconfigure(6, minsize=50)

    state.rowconfigure(0, minsize=50)
    state.rowconfigure(1, minsize=50)
    state.rowconfigure(2, minsize=50)
    state.rowconfigure(3, minsize=50)
    state.rowconfigure(4, minsize=50)
    state.rowconfigure(5, minsize=50)
    state.rowconfigure(6, minsize=50)
    state.resizable(False, False)

    # кнопки номеров

    room_1 = tk.Button(state, text='1', bg='green', bd=2, command=lambda: choice_room(1))
    room_1.grid(row=1, column=1, padx=3, pady=3, stick='wens')
    room_2 = tk.Button(state, text='2', bg='green', bd=2, command=lambda: choice_room(2))
    room_2.grid(row=1, column=2, padx=3, pady=3, stick='wens')
    room_3 = tk.Button(state, text='3', bg='green', bd=2, command=lambda: choice_room(3))
    room_3.grid(row=1, column=3, padx=3, pady=3, stick='wens')
    room_4 = tk.Button(state, text='4', bg='green', bd=2, command=lambda: choice_room(4))
    room_4.grid(row=1, column=4, padx=3, pady=3, stick='wens')
    room_5 = tk.Button(state, text='5', bg='green', bd=2, command=lambda: choice_room(5))
    room_5.grid(row=1, column=5, padx=3, pady=3, stick='wens')
    room_6 = tk.Button(state, text='6', bg='green', bd=2, command=lambda: choice_room(6))
    room_6.grid(row=2, column=1, padx=3, pady=3, stick='wens')
    room_7 = tk.Button(state, text='7', bg='green', bd=2, command=lambda: choice_room(7))
    room_7.grid(row=2, column=2, padx=3, pady=3, stick='wens')
    room_8 = tk.Button(state, text='8', bg='green', bd=2, command=lambda: choice_room(8))
    room_8.grid(row=2, column=3, padx=3, pady=3, stick='wens')
    room_9 = tk.Button(state, text='9', bg='green', bd=2, command=lambda: choice_room(9))
    room_9.grid(row=2, column=4, padx=3, pady=3, stick='wens')
    room_10 = tk.Button(state, text='10', bg='green', bd=2, command=lambda: choice_room(10))
    room_10.grid(row=2, column=5, padx=3, pady=3, stick='wens')
    room_11 = tk.Button(state, text='11', bg='green', bd=2, command=lambda: choice_room(11))
    room_11.grid(row=3, column=1, padx=3, pady=3, stick='wens')
    room_12 = tk.Button(state, text='12', bg='green', bd=2, command=lambda: choice_room(12))
    room_12.grid(row=3, column=2, padx=3, pady=3, stick='wens')
    room_13 = tk.Button(state, text='13', bg='green', bd=2, command=lambda: choice_room(13))
    room_13.grid(row=3, column=3, padx=3, pady=3, stick='wens')
    room_14 = tk.Button(state, text='14', bg='green', bd=2, command=lambda: choice_room(14))
    room_14.grid(row=3, column=4, padx=3, pady=3, stick='wens')
    room_15 = tk.Button(state, text='15', bg='green', bd=2, command=lambda: choice_room(15))
    room_15.grid(row=3, column=5, padx=3, pady=3, stick='wens')
    room_16 = tk.Button(state, text='16', bg='green', bd=2, command=lambda: choice_room(16))
    room_16.grid(row=4, column=1, padx=3, pady=3, stick='wens')
    room_17 = tk.Button(state, text='17', bg='green', bd=2, command=lambda: choice_room(17))
    room_17.grid(row=4, column=2, padx=3, pady=3, stick='wens')
    room_18 = tk.Button(state, text='18', bg='green', bd=2, command=lambda: choice_room(18))
    room_18.grid(row=4, column=3, padx=3, pady=3, stick='wens')
    room_19 = tk.Button(state, text='19', bg='green', bd=2, command=lambda: choice_room(19))
    room_19.grid(row=4, column=4, padx=3, pady=3, stick='wens')
    room_20 = tk.Button(state, text='20', bg='green', bd=2, command=lambda: choice_room(20))
    room_20.grid(row=4, column=5, padx=3, pady=3, stick='wens')
    room_21 = tk.Button(state, text='21', bg='green', bd=2, command=lambda: choice_room(21))
    room_21.grid(row=5, column=1, padx=3, pady=3, stick='wens')
    room_22 = tk.Button(state, text='22', bg='green', bd=2, command=lambda: choice_room(22))
    room_22.grid(row=5, column=2, padx=3, pady=3, stick='wens')
    room_23 = tk.Button(state, text='23', bg='green', bd=2, command=lambda: choice_room(23))
    room_23.grid(row=5, column=3, padx=3, pady=3, stick='wens')
    room_24 = tk.Button(state, text='24', bg='green', bd=2, command=lambda: choice_room(24))
    room_24.grid(row=5, column=4, padx=3, pady=3, stick='wens')
    room_25 = tk.Button(state, text='25', bg='green', bd=2, command=lambda: choice_room(25))
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

    for room in DICT:
        if room in j_dict["Room_repair"]:
            DICT[room]['bg'] = 'red'
        else:
            DICT[room]['state'] = tk.DISABLED
            DICT[room]['disabledforeground'] = 'grey'

    for guest in j_dict["Guests"]:
        try:
            room = str(j_dict["Guests"][guest]["Room"]["Number"])
        except Exception:
            pass
        else:
            DICT[room]['bg'] = 'grey'
            DICT[room]['state'] = tk.NORMAL
            DICT[room]['disabledforeground'] = 'black'

    state.mainloop()


if __name__ == '__main__':
    room_state_func()