# try:
#     file = open("yoli.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["abhinav"])
# except FileNotFoundError:
#     file = open("yoli.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# finally:
#     file.close()




height = float(input("Enter your height "))
if (height > 3):
    raise ValueError ("Human height does not tend over 3m // Enter a valid height ")
weight = int(input("Enter your weight "))

bmi = weight / height ** 2
print(bmi)


