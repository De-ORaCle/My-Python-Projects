'''As the name of the program suggests, we will be imitating a rolling dice.
This is one of the interesting python projects and will generate a random number each dice the program runs,
and the users can use the dice repeatedly for as long as he wants. When the user rolls the dice,
the program will generate a random number between 1 and 6 (as on a standard dice).

The number will then be displayed to the user. It will also ask users if they would like to roll the dice again.
The program should also include a function that can randomly grab a number within 1 to 6 and print it.
This beginner-level python projects will help build a strong foundation for fundamental programming concepts.

'''

while True:                                                                         #This line loops the rest of the code over and over infinititively
    print ("Roll the dice (Press Enter to continue) ")
    input ()
    import random
    dice = random.randint(1,6)                                                      #This line lets python choose any random number between 1 and 6
    print("--- ",dice)

    End = input ('''\nDo you wish to roll a dice again?
1. Yes
2. No
\n''')

    End = int(End)
    if End == 1:
        continue                                                                    #Provided the user chooses to continue, this line makes the loop continue
    elif End == 2:
        break
    else:
        print ("You entered an invalid input.")
        exit()
