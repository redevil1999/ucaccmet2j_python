import json

with open ('precipitation.json', encoding= 'utf8') as file:
    data = json.load(file)

#Exercise 1: calculate the monthly amount of rain in Seattle

#Step 1: identify the variables (months, year, amount of rain)
#month and year are specified in the json file by date
#amount of rain is specified by value

#step 2: Write a code to categorise the dates per month
#limit data to only the first 



months = [0]*12
month_value = {}
seattle = 'GHCND:US1WAKG0038'

for observation in data:
    if observation['station'] == seattle:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months[month] += observation['value']

print(months)

# print(months)
# print(f'In a year, the total amount of rain in Seattle is {sum(months)}')


#step 3: identify the values that are part of each month

#Step 4: create a total of the values
