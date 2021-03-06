import csv
from datetime import datetime

from matplotlib import pyplot as plt

file_name = 'death_valley_2014.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates,  highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title('Temperaturas máximas e minímas diárias  - 2014\n Death Valley,CA', fontsize='20')
    plt.xlabel('', fontsize='16')
    fig.autofmt_xdate()
    plt.ylabel('Temperatura(F)', fontsize='16')
    plt.tick_params(axis='both', which='major', labelsize='16')
    plt.show()
