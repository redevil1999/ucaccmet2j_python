import json

with open ('precipitation.json', encoding= 'utf8') as file:
    data = json.load(file)

#Exercise 1: calculate the monthly amount of rain in Seattle

#Step 1: identify the variables (months, year, amount of rain)
#month and year are specified in the json file by date
#amount of rain is specified by value

#step 2: Write a code to categorise the dates per month
#limit data to only the first 
months = []
month_value = {}
for observation in data:
    date = observation['date'].split('-')
    observation['date'] = [date[0], date[1]]
    #months.append(month)
    # if month in data:
    #     data[month] += int(data['value'])
    # else:
    #     data[month] - 
#print(months)
print(data)
# for date in months:
    
#     months.append(month)
# print(months)

#step 3: identify the values that are part of each month

#Step 4: create a total of the values
