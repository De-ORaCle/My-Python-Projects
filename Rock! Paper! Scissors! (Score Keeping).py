'''
If you are tired of having no playmate, then a 5-minute stint of rock, paper,
scissors with the computer and designed by you, yourself will improve your mood.

We again use the random function here.
You make a move first and then the program makes one.
To indicate the move, you can either use a single alphabet or input an entire string.
A function will have to be set up to check the validity of the move.

Using another function, the winner of that round is decided.
You can then either give an option of playing again or decide a pre-determined number of moves in advance.
A scorekeeping function will also have to be created which will return the winner at the end.
'''

import random
bot = random.randint(1,3)                                   #Making python generate a random integer between 1-3
score = 0                                                   #Creating a variable to store the user's score
loop = 0                                                    #Creating a variable to store the user's total number of trials

while True:                                                 #Looping the code till it is instructed to stopb
    loop = loop + 1
    print ("Rock! Paper! Scissors!\n")
    userput = input('''Enter 1 for Rock!
Enter 2 for Paper!
Enter 3 for Scissors!\n
''')                                                        #Collecting a simple input from the user

    if userput.isdigit():                                   #Making sure the user entered a digit
        print ("")
    else:
        print ("You didn't enter a number!")
        break

    if bot == 1:                                            #Assigning the bot's random numbers to variables in the real game
        botput = "Rock!"
    elif bot == 2:
        botput = "Paper!"
    elif bot == 3:
        botput = "Scissors!"
    else:                                                   #An impossible situation
        print ("I think I might have a mental breakdown.")
        break
