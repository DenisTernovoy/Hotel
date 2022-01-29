import tkinter as tk
import json
from change_room import change_room_main


def accept_all(num):
    btn_1['state'] = tk.DISABLED
    ID = num
    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)

    if ld['value'] == 1:
        j_dict['Guests'][ID]['Departure']['Time'] = "18:00"

    temp = {}

    temp['Breakfast'] = br['value'] * 1000
    j_dict['Guests'][ID]['Services']['Breakfast'] = j_dict['Guests'][ID]['Services']['Breakfast'] + br['value']

    temp['Parking'] = par['value'] * 1000
    j_dict['Guests'][ID]['Services']['Parking'] = j_dict['Guests'][ID]['Services']['Parking'] + par['value']

    if j_dict['Guests'][ID]['Services']['Extra_bed'] == 1:
        pass
    else:
        temp['Extra_bed'] = bd['value'] * 500
        j_dict['Guests'][ID]['Services']['Extra_bed'] = j_dict['Guests'][ID]['Services']['Extra_bed'] + bd['value']

    temp['Room_clean'] = cln['value'] * 300
    j_dict['Guests'][ID]['Services']['Room_clean'] = j_dict['Guests'][ID]['Services']['Room_clean'] + cln['value']

    temp['Chem_clean'] = chem_cln['value'] * 2000
    j_dict['Guests'][ID]['Services']['Chem_clean'] = j_dict['Guests'][ID]['Services']['Chem_clean'] + chem_cln['value']

    temp['Teeth_kit'] = th['value'] * 100
    j_dict['Guests'][ID]['Services']['Teeth_kit'] = j_dict['Guests'][ID]['Services']['Teeth_kit'] + th['value']

    temp['Sew_kit'] = sw['value'] * 100
    j_dict['Guests'][ID]['Services']['Sew_kit'] = j_dict['Guests'][ID]['Services']['Sew_kit'] + sw['value']

    if j_dict['Guests'][ID]['Services']['Late_departure'] == 1:
        j_dict['Guests'][ID]['Departure']['Time'] = "18:00"
        pass
    else:
        temp['Late_departure'] = ld['value'] * 1500
        j_dict['Guests'][ID]['Services']['Late_departure'] = j_dict['Guests'][ID]['Services']['Late_departure'] + \
                                                             ld['value']


    total = 0
    for i in temp:
        total += temp[i]

    temp['Total'] = total

    if total > 0:
        j_dict['Guests'][ID]['Changes'].append(temp)

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

    total = tk.Label(wcs, text=f"Total: {temp['Total']} руб.",
                     font=('Arial', 16, 'bold'))
    total.grid(row=20, column=1, columnspan=4, stick='wens')

    tk.Button(wcs, text='Принять оплату',
              command=lambda: wcs.destroy()).grid(row=20, column=5, columnspan=2, stick='wens')


def analyze(service, change):
    if change == -1 and service['value'] == 0:
        pass
    elif service['name'] == 'Extra bed' or service['name'] == 'Late departure':
        if service['value'] == -1 or (service['value'] == 1 and change != -1):
            pass
        else:
            service['value'] += change
            service['param'].delete(0, tk.END)
            service['param'].insert(0, f"{service['name']}: {service['value']}")
    else:
        service['value'] += change
        service['param'].delete(0, tk.END)
        service['param'].insert(0, f"{service['name']}: {service['value']}")


def change_services(num):
    global br, par, bd, cln, chem_cln, th, sw, ld, wcs, btn_1
    ID = num
    win_change.destroy()

    # конфигурация главного окна

    wcs = tk.Tk()
    wcs.title('Изменение услуг')

    wcs.geometry("480x860+700+100")

    wcs.columnconfigure(0, minsize=60)
    wcs.columnconfigure(1, minsize=60)
    wcs.columnconfigure(2, minsize=60)
    wcs.columnconfigure(3, minsize=60)
    wcs.columnconfigure(4, minsize=60)
    wcs.columnconfigure(5, minsize=60)
    wcs.columnconfigure(6, minsize=60)
    wcs.columnconfigure(7, minsize=60)

    wcs.rowconfigure(0, minsize=40)
    wcs.rowconfigure(1, minsize=40)
    wcs.rowconfigure(2, minsize=40)
    wcs.rowconfigure(3, minsize=40)
    wcs.rowconfigure(4, minsize=40)
    wcs.rowconfigure(5, minsize=40)
    wcs.rowconfigure(6, minsize=40)
    wcs.rowconfigure(7, minsize=40)
    wcs.rowconfigure(8, minsize=40)
    wcs.rowconfigure(9, minsize=40)
    wcs.rowconfigure(10, minsize=40)
    wcs.rowconfigure(11, minsize=40)
    wcs.rowconfigure(12, minsize=40)
    wcs.rowconfigure(13, minsize=40)
    wcs.rowconfigure(14, minsize=40)
    wcs.rowconfigure(15, minsize=40)
    wcs.rowconfigure(16, minsize=40)
    wcs.rowconfigure(17, minsize=30)
    wcs.rowconfigure(18, minsize=30)
    wcs.rowconfigure(19, minsize=30)
    wcs.rowconfigure(20, minsize=30)

    wcs.resizable(False, False)

    tk.Label(wcs, text="Каталог услуг",
             bg='#D0D5DE',
             font=("Arial", 18, 'bold')
             ).grid(row=0, column=0, columnspan=8, stick='wens')

    btn_1 = tk.Button(wcs, text='Принять', command=lambda: accept_all(ID))
    btn_1.grid(row=18, column=3, columnspan=2, stick='wens')

    # услуги

    breakfast = tk.Entry(wcs)
    br = {'name': 'Extra breakfast', 'value': 0, 'param': breakfast}
    breakfast.grid(row=2, column=3, columnspan=2, stick='wens')
    breakfast.insert(0, f'{br["name"]}: {br["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(br, 1)).grid(row=2, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(br, -1)).grid(row=2, column=1, stick='wens')

    parking = tk.Entry(wcs)
    par = {'name': 'Extra parking', 'value': 0, 'param': parking}
    parking.grid(row=4, column=3, columnspan=2, stick='wens')
    parking.insert(0, f'{par["name"]}: {par["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(par, 1)).grid(row=4, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(par, -1)).grid(row=4, column=1, stick='wens')

    bed = tk.Entry(wcs)
    bd = {'name': 'Extra bed', 'value': 0, 'param': bed}
    bed.grid(row=6, column=3, columnspan=2, stick='wens')

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)
        if j_dict['Guests'][ID]['Services']['Extra_bed'] == 1:
            bed.insert(0, f'{bd["name"]}: 1')
            bd['value'] = -1
        else:
            bed.insert(0, f'{bd["name"]}: 0')
            tk.Button(wcs, text='+1', command=lambda: analyze(bd, 1)).grid(row=6, column=6, stick='wens')
            tk.Button(wcs, text='-1', command=lambda: analyze(bd, -1)).grid(row=6, column=1, stick='wens')

    clean = tk.Entry(wcs)
    cln = {'name': 'Extra clean', 'value': 0, 'param': clean}
    clean.grid(row=8, column=3, columnspan=2, stick='wens')
    clean.insert(0, f'{cln["name"]}: {cln["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(cln, 1)).grid(row=8, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(cln, -1)).grid(row=8, column=1, stick='wens')

    chem_clean = tk.Entry(wcs)
    chem_cln = {'name': 'Extra chem_clean', 'value': 0, 'param': chem_clean}
    chem_clean.grid(row=10, column=3, columnspan=2, stick='wens')
    chem_clean.insert(0, f'{chem_cln["name"]}: {chem_cln["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(chem_cln, 1)).grid(row=10, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(chem_cln, -1)).grid(row=10, column=1, stick='wens')

    teeth = tk.Entry(wcs)
    th = {'name': 'Extra teeth_kit', 'value': 0, 'param': teeth}
    teeth.grid(row=12, column=3, columnspan=2, stick='wens')
    teeth.insert(0, f'{th["name"]}: {th["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(th, 1)).grid(row=12, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(th, -1)).grid(row=12, column=1, stick='wens')

    sew = tk.Entry(wcs)
    sw = {'name': 'Extra sew_kit', 'value': 0, 'param': sew}
    sew.grid(row=14, column=3, columnspan=2, stick='wens')
    sew.insert(0, f'{sw["name"]}: {sw["value"]}')

    tk.Button(wcs, text='+1', command=lambda: analyze(sw, 1)).grid(row=14, column=6, stick='wens')
    tk.Button(wcs, text='-1', command=lambda: analyze(sw, -1)).grid(row=14, column=1, stick='wens')

    late_d = tk.Entry(wcs)
    ld = {'name': 'Late departure', 'value': 0, 'param': late_d}
    late_d.grid(row=16, column=3, columnspan=2, stick='wens')

    with open('data.json', 'r') as json_file:
        j_dict = json.load(json_file)
        if j_dict['Guests'][ID]['Services']['Late_departure'] == 1:
            j_dict['Guests'][ID]['Departure']['Time'] = "18:00"
            late_d.insert(0, f'{ld["name"]}: 1')
            ld['value'] = -1
        else:
            late_d.insert(0, f'{ld["name"]}: 0')
            tk.Button(wcs, text='+1', command=lambda: analyze(ld, 1)).grid(row=16, column=6, stick='wens')
            tk.Button(wcs, text='-1', command=lambda: analyze(ld, -1)).grid(row=16, column=1, stick='wens')

    wcs.mainloop()


def change_room(num):
    ID = num
    win_change.destroy()
    change_room_main(ID)



def main_change(num):
    global win_change
    ID = num

    # конфигурация главного окна

    win_change = tk.Tk()

    win_change.geometry('350x300+750+250')

    win_change.rowconfigure(0, minsize=60)
    win_change.rowconfigure(1, minsize=60)
    win_change.rowconfigure(2, minsize=60)
    win_change.rowconfigure(3, minsize=60)
    win_change.rowconfigure(4, minsize=60)

    win_change.columnconfigure(0, minsize=70)
    win_change.columnconfigure(1, minsize=70)
    win_change.columnconfigure(2, minsize=70)
    win_change.columnconfigure(3, minsize=70)
    win_change.columnconfigure(4, minsize=70)

    win_change.resizable(False, False)

    # кнопки

    tk.Button(win_change, text='Изменить услуги', command=lambda: change_services(ID)).grid(row=1, column=1, columnspan=3, stick='wens')

    tk.Button(win_change, text='Изменить комнату', command=lambda: change_room(ID)).grid(row=3, column=1, columnspan=3, stick='wens')

    win_change.mainloop()






if __name__ == '__main__':
    main_change('1_1')