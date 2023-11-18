PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print("Names:")
    print (names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_cont = letter_file.read()
    for name in names:
        name = name.strip("\n")
        new_letter = letter_cont.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invitation:
            invitation.write(new_letter)