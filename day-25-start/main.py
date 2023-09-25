# with open ("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
# print (temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data['temp'].mean())
#
# monday = data[data['day'] == 'Monday']
# temp = int(monday['temp'])
# tempf = temp * 9/5 + 32
#
# print(tempf)

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(df.columns)
# gray = len((df[df['Primary Fur Color'] == "Gray"]))
# cinnamon = len((df[df['Primary Fur Color'] == "Cinnamon"]))
# black = len((df[df['Primary Fur Color'] == "Black"]))

gray_squirrels = len(df[df['Primary Fur Color'] == "Gray"])
red_squirrels = len(df[df['Primary Fur Color'] == "Cinnamon"])
black_squirrels = len(df[df['Primary Fur Color'] == "Black"])

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df_new = pd.DataFrame(data_dict)
df_new.to_csv("squirrel_count.csv")