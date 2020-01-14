import json

with open ('precipitation.json', encoding= 'utf8') as file:
    data = json.load(file)

#Exercise 1: calculate the monthly amount of rain in Seattle

#Step 1: identify the variables (months, year, amount of rain)
#month and year are specified in the json file by date
#amount of rain is specified by value

#step 2: Write a code to categorise the dates per month
#limit data to only the first 

#In the following, the code calculates the amount of rain per month per station. 
#First, the station name is used to select only the station in Seattle
#Second, it adds each value per month
months_seattle = [0]*12
seattle = 'GHCND:US1WAKG0038'

for observation in data:
    if observation['station'] == seattle:
            date = observation['date'].split('-')
            month = int(date[1]) -1
            months_seattle[month] += observation['value']

print(months_seattle)
total_rain = sum(months_seattle)

#The second assignment requested the percentage per month of the full year.
#In the following, you can see the percentage calculations.

percentage_per_month = []
for month in months_seattle:
    percentage = (month/total_rain)*100
    percentage_per_month.append(percentage)
    print(percentage)

seattle_monthly_amount_and_percentage = {}
seattle_monthly_amount_and_percentage['Amount per month'] = months_seattle
seattle_monthly_amount_and_percentage['Percentage per month'] = percentage_per_month

print(seattle_monthly_amount_and_percentage)

with open('monthly_rain_seattle.json', 'w', encoding='utf8') as file:
     json.dump(seattle_monthly_amount_and_percentage, file)