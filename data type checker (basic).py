#This program receives input from a user and tell the user which basic python data type the input is.

word = input("Enter a number or text: ")

if word.isalpha():
    print("You entered a string")
else:
    if word.isdigit():
        print ("You entered an integer")
    else:
        print ("You entered a float")
