word = input("Enter a number or text: ")

if word.isalpha():
    print("You entered a string")
else:
    if word.isdigit():
        print ("You entered an integer")
    else:
        print ("You entered a float")
