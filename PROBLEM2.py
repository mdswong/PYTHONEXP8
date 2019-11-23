"""
PROBLEM 2
Using the dataframe "cars" in the previous problem, extract the following
information using subsetting, slicing, and indexing operations.

a) Display the first five rows with odd-numbered columns of "cars".
b) Display the row that contains the 'Model' of 'Mazda RX4'.
c) How many cylinders ('cyl') does the car model 'Camaro Z28' have?
d) Determine how many cylinders ('cyl') and what gear type ('gear') do the car
models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
"""

import pandas as pd

cars = pd.read_csv('cars.csv')
df = cars

print('\n')

print('First five rows with odd-numbered columns of cars: \n')
print(df.iloc[0:5, [1,3,5,7,9,11]])
print('\n')

print('Row that contains the "Model" of "Mazda RX4": \n')
print(df[df['Model']=='Mazda RX4'])
print('\n')

print('Number of cylinders of the car model "Camaro Z28": \n')
print(df.loc[[23],['Model', 'cyl']])
print('\n')

print('Number of Cylinders and Gear Type of three (3) car models: \n')
print(df.loc[[1,18,28],['Model', 'cyl', 'gear']])