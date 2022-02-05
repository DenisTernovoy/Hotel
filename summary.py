import tkinter as tk
import json
import datetime as dt


def main_summary(num):
    ID = num
    with open("data.json", 'r') as json_file:
        j_dict = json.load(json_file)

        if j_dict['Guests'][ID]['Services']['Breakfast'] != 0:
            j_dict['Guests'][ID]['Summary']['Breakfast'] = j_dict['Guests'][ID]['Services']['Breakfast'] * 1000
        if j_dict['Guests'][ID]['Services']['Parking'] != 0:
            j_dict['Guests'][ID]['Summary']['Parking'] = j_dict['Guests'][ID]['Services']['Parking'] * 1000
        if j_dict['Guests'][ID]['Services']['Extra_bed'] == 1:
            j_dict['Guests'][ID]['Summary']['Extra_bed'] = 500
        if j_dict['Guests'][ID]['Services']['Room_clean'] != 0:
            j_dict['Guests'][ID]['Summary']['Room_clean'] = j_dict['Guests'][ID]['Services']['Room_clean'] * 300
        if j_dict['Guests'][ID]['Services']['Chem_clean'] != 0:
            j_dict['Guests'][ID]['Summary']['Chem_clean'] = j_dict['Guests'][ID]['Services']['Chem_clean'] * 2000
        if j_dict['Guests'][ID]['Services']['Teeth_kit'] != 0:
            j_dict['Guests'][ID]['Summary']['Teeth_kit'] = j_dict['Guests'][ID]['Services']['Teeth_kit'] * 100
        if j_dict['Guests'][ID]['Services']['Sew_kit'] != 0:
            j_dict['Guests'][ID]['Summary']['Sew_kit'] = j_dict['Guests'][ID]['Services']['Sew_kit'] * 100
        if j_dict['Guests'][ID]['Services']['Early_arrival'] == 1:
            j_dict['Guests'][ID]['Summary']['Early_arrival'] = 1500
        if j_dict['Guests'][ID]['Services']['Late_departure'] == 1:
            j_dict['Guests'][ID]['Summary']['Late_departure'] = 1500
        if j_dict['Guests'][ID]['Services']['Night_arrival'] == 1:
            j_dict['Guests'][ID]['Summary']['Night_arrival'] = 3000
        if j_dict['Guests'][ID]['Services']['Room_upgrade'] == 1:
            date_now = dt.date.today()
            day = int(j_dict['Guests'][ID]['Departure']['Date'][:2])
            month = int(j_dict['Guests'][ID]['Departure']['Date'][3:5])
            year = int(j_dict['Guests'][ID]['Departure']['Date'][6:10])
            date_departure = dt.date(year, month, day)
            day_stay = date_departure - date_now
            stay = int(day_stay.days)
            if dt.time(0, 00, 00) < dt.datetime.now().time() < dt.time(5, 00, 00):
                stay += 1
            j_dict['Guests'][ID]['Summary']['Room_upgrade'] = stay * 1500

        total = 0
        for i in j_dict['Guests'][ID]['Summary']:
            total += j_dict['Guests'][ID]['Summary'][i]

        for i in j_dict['Guests'][ID]['Changes'][:len(j_dict['Guests'][ID]['Changes']) - 1]:
            if 'Late_departure' in i:
                total += i['Late_departure']

        for i in j_dict['Guests'][ID]['Changes'][:len(j_dict['Guests'][ID]['Changes'])]:
            if 'Room_move' in i:
                total += i['Total']

        with open('data.json', 'w') as json_file:
            json.dump(j_dict, json_file, indent=4)

        return total


if __name__ == '__main__':
    main_summary('1_1')