import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    row_header = next(reader)

    #for index, column_header in enumerate(row_header):
    #    print (index, column_header)
        #get date and high tempreture from the the file
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low =int (row[5])
        except ValueError:
            print(f'missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)   

# Plot the low and high temperatures.
plt.style.use ('seaborn')
fig , ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# format plot
title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
plt.title(title, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()       # draws the date labels diagonally to prevent them from overlapping
plt.ylabel('tempreture (F)', fontsize = 16)
plt.tick_params('both', which='major', labelsize = 16)
#plt.axis ([0,30,50,72])
plt.show()