# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass


file = pandas.read_csv("nato_phonetic_alphabet.csv")

# for (index, row) in file.iterrows():
#     print(row.letter)

new_dict = {row.letter: row.code for (index, row) in file.iterrows()}
# print(new_dict)



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on = True

while is_on:
    user_data = input("Enter your name: ").upper()

    try:
        if user_data == "":
            raise ValueError("Enter something")
        user_dict = [new_dict[n] for n in user_data]
    except ValueError:
        print("Enter something")

    except KeyError:
        print("Sorry only alphabets allowed")
    else:
        print(user_dict)
        is_on = False


