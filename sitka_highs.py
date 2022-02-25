import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename ='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index , culomn_header in enumerate(header_row):
    #    print (index,culomn_header)

    #get date and high tempreture from the the file
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low =int (row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)   

# Plot the low and high temperatures.
plt.style.use ('seaborn')
fig , ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
# format plot
plt.title('daily high and low tempreture - 2018', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()       # draws the date labels diagonally to prevent them from overlapping
plt.ylabel('tempreture (F)', fontsize = 16)
plt.tick_params('both', which='major', labelsize = 16)
#plt.axis ([0,30,50,72])
plt.show()