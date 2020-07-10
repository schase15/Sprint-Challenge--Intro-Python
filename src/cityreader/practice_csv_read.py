# Blank page to read in the csv and add each 
# to a list before implementing it into my class as a method

from cityreader import City
# import pandas as pd



# def city_reader(csv):
#     df = pd.read_csv(csv)

#     list_city = []

#     for i in range(df.shape[0]):
#         list_city.append(City(df['city'][i], df['lat'][i], df['lng'][i]))

#     print(list_city)


# city_reader('cities.csv')


# Read the csv in with python
# set range to do each row except for the first one
# Use the indecies to call the specific columns you need

city = []

import csv

def city_reader_1(city = []):
    with open('cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                city.append(City(row[0], row[3], row[4]))
                line_count += 1
    return city

city_reader_1(city)

for c in city:
    print(c)