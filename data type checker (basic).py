#This program receives input from a user and tells the user which basic python data type the input is.

word = input("Enter a number or text: ")

if word.isalpha():                                             #This line processes all alphabets inputs as strings
    print("You entered a string")
else:                                                          #Since I couldn't find a function to differentiate integers and floats, I had to note that since alphabets have been selected and floats are not considered digits, the isdigit() function would work well.
    if word.isdigit():
        print ("You entered an integer")
    else:
        print ("You entered a float")
