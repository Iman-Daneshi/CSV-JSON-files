import csv
import matplotlib.pyplot as plt

filename ='data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index , culomn_header in enumerate(header_row):
    #    print (index,culomn_header)

    #get high tempreture from the the file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)   

# Plot the high temperatures.
plt.style.use ('seaborn')
fig , ax = plt.subplots()
ax.plot(highs, c='red')
# format plot
plt.title('daily high tempreture, July 2018', fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('tempreture (F)', fontsize = 16)
plt.tick_params('both', which='major', labelsize = 16)
#plt.axis ([0,30,50,72])
plt.show()