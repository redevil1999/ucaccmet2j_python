import json

with open ('precipitation.json', encoding= 'utf8') as file:
    data = json.load(file)

#Exercise 1: calculate the monthly amount of rain in Seattle

#Step 1: identify the variables (months, year, amount of rain)
#month and year are specified in the json file by date
#amount of rain is specified by value

#step 2: Write a code to categorise the dates per month
#limit data to only the first 

months_seattle = [0]*12
seattle = 'GHCND:US1WAKG0038'

for observation in data:
    if observation['station'] == seattle:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months_seattle[month] += observation['value']

months_cincinnati = [0]*12
cincinnati = 'GHCND:USW00093814'

for observation in data:
    if observation['station'] == cincinnati:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months_cincinnati[month] += observation['value']

months_maui = [0]*12
maui = 'GHCND:USC00513317'

for observation in data:
    if observation['station'] == maui:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months_maui[month] += observation['value']

months_sandiego = [0]*12
sandiego = 'GHCND:US1CASD0032'

for observation in data:
    if observation['station'] == sandiego:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months_sandiego[month] += observation['value']

print(f'Seattle per month {months_seattle}')
print(f'Cincinnati per month {months_cincinnati}')
print(f'Maui per month {months_maui}')
print(f'San Diego per month {months_sandiego}')
print(f'In a year, the total amount of rain at these four stations is {sum(months_seattle) + sum(months_cincinnati) + sum(months_maui) + sum(months_sandiego)}')

