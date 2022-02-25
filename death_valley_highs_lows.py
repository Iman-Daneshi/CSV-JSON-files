import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    row_header = next(reader)

    for index, column_header in enumerate(row_header):
        print (index, column_header)