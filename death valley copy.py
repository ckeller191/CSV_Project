# 1. handle error checking using try and except
# 2. change file to use death valley data


import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)

highs = []
dates = []
lows = []



for row in csv_file:
    try: 
        high = int(row[4])
        low = int(row[5]) 
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

#print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel('', fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()

fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

plt.show()