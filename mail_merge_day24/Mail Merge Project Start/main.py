# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    # print(contents)
#

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    names = f.readlines()

names_without_space = []

for p in names:
    x = p.strip()
    names_without_space.append(x)
    with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as f:
        y = contents.replace("[name]", f"{p}")

    with open(f"../Mail Merge Project Start/Output/ReadyToSend/{x}", mode="a") as files:
        new_item = files.write(f"\n{y}")

