import string
import random

length = int(input("Enter the length of the password: "))
if (length < 4):
    print(f"WARNING!!! {length} is too short.")

print('''Please choose a set of characters from these options for your strong password:
        1. Letters
        2. Numbers
        3. Punctuation / Special characters
        4. Exit''')

characterList = "" # creating a string

# Getting charcters for Password
chances = 0
while(chances < 4):
    choice = int(input("Pick a Number: "))
    chances += 1
    if (choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please choose a valid option")

password = []

for i in range(length):
    randomchar = random.choice(characterList) # choice() returns a random item

    password.extend(randomchar) # extend() is adding items of randomchar to list password

print("Your  " + "".join(password))
