import csv
from datetime import datetime

from matplotlib import pyplot as plt

file_name = 'sitka_weather_2014.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates,  highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        low = int(row[3])
        lows.append(low)
        high = int(row[1])
        highs.append(high)

    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title('Temperaturas máximas e minímas diárias  - 2014', fontsize='24')
    plt.xlabel('', fontsize='16')
    fig.autofmt_xdate()
    plt.ylabel('Temperatura(F)', fontsize='16')
    plt.tick_params(axis='both', which='major', labelsize='16')
    plt.show()
