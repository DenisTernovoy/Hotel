import tkinter as tk
import json


def main_bills(num):
    ID = num
    # конфигурация главного окна

    win_bill = tk.Tk()
    win_bill.title('Чеки оплаты')

    win_bill.geometry("480x860+700+100")

    win_bill.columnconfigure(0, minsize=60)
    win_bill.columnconfigure(1, minsize=60)
    win_bill.columnconfigure(2, minsize=60)
    win_bill.columnconfigure(3, minsize=60)
    win_bill.columnconfigure(4, minsize=60)
    win_bill.columnconfigure(5, minsize=60)
    win_bill.columnconfigure(6, minsize=60)
    win_bill.columnconfigure(7, minsize=60)

    win_bill.rowconfigure(0, minsize=40)
    win_bill.rowconfigure(1, minsize=40)
    win_bill.rowconfigure(2, minsize=40)
    win_bill.rowconfigure(3, minsize=40)
    win_bill.rowconfigure(4, minsize=40)
    win_bill.rowconfigure(5, minsize=40)
    win_bill.rowconfigure(6, minsize=40)
    win_bill.rowconfigure(7, minsize=40)
    win_bill.rowconfigure(8, minsize=40)
    win_bill.rowconfigure(9, minsize=40)
    win_bill.rowconfigure(10, minsize=40)
    win_bill.rowconfigure(11, minsize=40)
    win_bill.rowconfigure(12, minsize=40)
    win_bill.rowconfigure(13, minsize=40)
    win_bill.rowconfigure(14, minsize=40)
    win_bill.rowconfigure(15, minsize=40)
    win_bill.rowconfigure(16, minsize=40)
    win_bill.rowconfigure(17, minsize=30)
    win_bill.rowconfigure(18, minsize=30)
    win_bill.rowconfigure(19, minsize=30)
    win_bill.rowconfigure(20, minsize=30)

    win_bill.resizable(False, False)

    tk.Label(win_bill, text="Чеки",
             bg='#D0D5DE',
             font=("Arial", 18, 'bold')
             ).grid(row=0, column=0, columnspan=8, stick='wens')

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

    row = 1

    if 'Share' not in j_dict['Guests'][ID]:
        tk.Label(win_bill, text="Стартовый чек:",
                 font=("Arial", 14, 'bold')
                 ).grid(row=1, column=0, columnspan=8, stick='w')

        tk.Label(win_bill, text=f"Количество ночей: {j_dict['Guests'][ID]['Stay']}").\
            grid(row=2, column=0, columnspan=8, stick='wens')

        row = 3

        for i in j_dict['Guests'][ID]['Changes'][0]:
            if j_dict['Guests'][ID]['Changes'][0][i] != 0:
                if i != 'Date' and i != 'Total':
                    tk.Label(win_bill, text=f"{i}: {j_dict['Guests'][ID]['Changes'][0][i]}"). \
                        grid(row=row, column=0, columnspan=8, stick='wens')
                    row += 1
        tk.Label(win_bill, text=f" Total: {j_dict['Guests'][ID]['Changes'][0]['Total']} руб.",
                 font=("Arial", 12, 'bold')). \
            grid(row=row, column=0, columnspan=8, stick='wens')

        row += 1

        tk.Label(win_bill, text="Доп услуги:",
                 font=("Arial", 14, 'bold')
                 ).grid(row=row, column=0, columnspan=8, stick='w')

        row += 1
        count = 1

        for i in j_dict['Guests'][ID]['Changes'][1:]:
            tk.Label(win_bill, text=f"{i['Date']}"). \
                grid(row=row, column=0, columnspan=8, stick='e')
            count += 1
            for j in i:
                if j != 'Date' and j != 'Total':
                    if i[j] != 0:
                        tk.Label(win_bill, text=f"{j}: {i[j]}"). \
                            grid(row=row, column=0, columnspan=8, stick='w')
                        row += 1
            tk.Label(win_bill, text=f"{'Total'}: {i['Total']} руб.",
                     font=("Arial", 12, 'bold')). \
                grid(row=row, column=0, columnspan=8, stick='wens')
            row += 1
    else:
        tk.Label(win_bill, text="Доп услуги:",
                 font=("Arial", 14, 'bold')
                 ).grid(row=row, column=0, columnspan=8, stick='w')

        row += 1
        count = 1

        for i in j_dict['Guests'][ID]['Changes'][0:]:
            tk.Label(win_bill, text=f"{i['Date']}"). \
                grid(row=row, column=0, columnspan=8, stick='e')
            count += 1
            for j in i:
                if j != 'Date' and j != 'Total':
                    if i[j] != 0:
                        tk.Label(win_bill, text=f"{j}: {i[j]}"). \
                            grid(row=row, column=0, columnspan=8, stick='w')
                        row += 1
            tk.Label(win_bill, text=f"{'Total'}: {i['Total']} руб.",
                     font=("Arial", 12, 'bold')). \
                grid(row=row, column=0, columnspan=8, stick='wens')
            row += 1
    # btn_1 = tk.Button(wcs, text='Принять', command=lambda: accept_all(ID))
    # btn_1.grid(row=18, column=3, columnspan=2, stick='wens')


if __name__ == '__main__':
    main_bills('1_1')
