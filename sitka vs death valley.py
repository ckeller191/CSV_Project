import csv
from datetime import datetime


#sitka file

sitka_open = open("sitka_weather_2018_simple.csv", "r")

sitka_file = csv.reader(sitka_open, delimiter= ",")

header_sitka = next(sitka_file)

header_dict_sitka = {}


for index, column_header in enumerate(header_sitka):
    print("Index: ", index, "Column Name: ", column_header)
    header_dict_sitka[column_header] = index

print(header_dict_sitka)


#Death Valley File

valley_open = open("death_valley_2018_simple.csv", "r")

valley_file = csv.reader(valley_open, delimiter= ",")

header_valley = next(valley_file)

header_dict_valley = {}

for index, column_header in enumerate(header_valley):
    print("Index: ", index, "Column Name: ", column_header)
    header_dict_valley[column_header] = index

print(header_dict_valley)

#make empty lists

s_highs = []
s_dates = []
s_lows = []
s_names = []

v_highs = []
v_dates = []
v_lows = []
v_names = []
#set auto indexes

s_high_index = header_dict_sitka["TMAX"]
s_low_index = header_dict_sitka["TMIN"]
s_date_index = header_dict_sitka["DATE"]
s_name_index = header_dict_sitka["NAME"]

v_high_index = header_dict_valley["TMAX"]
v_low_index = header_dict_valley["TMIN"]
v_date_index = header_dict_valley["DATE"]
v_name_index = header_dict_valley["NAME"]

#add to lists

for row in sitka_file:
    try:
        s_high = int(row[s_high_index])
        s_low = int(row[s_low_index])
        s_converted_date = datetime.strptime(row[s_date_index], "%Y-%m-%d")
        s_name = str(row[s_name_index])
    except ValueError:
        print(f"missing data for {s_converted_date}")
    else:
        s_highs.append(s_high)
        s_lows.append(s_low)
        s_dates.append(s_converted_date)
        s_names.append(s_name)


for row in valley_file:
    try:
        v_high = int(row[v_high_index])
        v_low = int(row[v_low_index])
        v_converted_date = datetime.strptime(row[v_date_index], "%Y-%m-%d")
        v_name = row[v_name_index]
    except ValueError:
        print(f"missing data for {s_converted_date}")
    else:
        v_highs.append(v_high)
        v_lows.append(v_low)
        v_dates.append(v_converted_date)
        v_names.append(v_name)


#create plot 

import matplotlib.pyplot as plt

fig, a = plt.subplots(2)

a[0].plot(s_dates, s_highs, c='red')
a[0].plot(s_dates, s_lows, c='blue')




a[1].plot(v_dates, v_highs, c='red')
a[1].plot(v_dates, v_lows, c='blue')

fig.autofmt_xdate()

a[0].fill_between(s_dates, s_highs, s_lows, facecolor='blue', alpha=0.1)
a[1].fill_between(v_dates, v_highs, v_lows, facecolor='blue', alpha=0.1)

plt.show()


