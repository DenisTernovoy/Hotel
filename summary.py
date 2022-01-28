import tkinter as tk
import json


def main_summary(num):
    ID = num
    with open("data.json", 'r') as json_file:
        j_dict = json.load(json_file)

        if j_dict['Guests'][ID]['Services']['Add_bed'] == 1:
            j_dict['Guests'][ID]['Summary']['Add_bed'] = 500
        if j_dict['Guests'][ID]['Services']['Add_clean'] == 1:
            j_dict['Guests'][ID]['Summary']['Add_clean'] = 0
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

    with open('data.json', 'w') as json_file:
        json.dump(j_dict, json_file, indent=4)

        total = 0
        for i in j_dict['Guests'][ID]['Summary']:
            total += j_dict['Guests'][ID]['Summary'][i]

        return total


if __name__ == '__main__':
    main_summary('1_1')