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
    highs ,dates = [] , []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)   

# Plot the high temperatures.
plt.style.use ('seaborn')
fig , ax = plt.subplots()
ax.plot(dates, highs, c='red')
# format plot
plt.title('daily high tempreture - 2018', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('tempreture (F)', fontsize = 16)
plt.tick_params('both', which='major', labelsize = 16)
#plt.axis ([0,30,50,72])
plt.show()