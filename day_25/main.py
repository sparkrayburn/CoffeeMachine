# # with open("weather_data.csv") as f:
# #     data = f.readlines()
# temperature = []
#
# new_data = []
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             new_data.append(int(row[1]))
#     print(new_data)
#


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

# temp_data = data["temp"]
# temp_list = temp_data.tolist()
# print(temp_list)
# print(data[data.temp == temp_data.max()])
# monday = data[data.temp == 12]
#
# converter = monday.temp *9/5 + 32
#
# print(converter)


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
#
# }
#
#
# file = pandas.DataFrame(data_dict)
# file.to_csv("myfiles.csv")


colors = data["Primary Fur Color"]
gray = colors[colors == "Gray"]
black = colors[colors == "Black"]
cinnamon = colors[colors == "Cinnamon"]

# print(len(black))
all_squirrels = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [len(gray), len(black), len(cinnamon)]

}

the_list = pandas.DataFrame(all_squirrels)

the_list.to_csv("togo_squirrels.csv")
