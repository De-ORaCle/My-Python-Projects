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

    userput = int(userput)

    if userput == 1:                                        #Assigning the simple inputs to the real game
        userinput = "Rock!"
    elif userput == 2:
        userinput = "Paper!"
    elif userput == 3:
        userinput = "Scissors!"
    else:
        print ("You didn't enter 1, 2 or 3.")
        break

    if bot == 1 and userput == 1:                           #The nine possible out comes and who wins in each
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nThat's a draw.")
    elif bot == 2 and userput == 2:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nThat's a draw.")
    elif bot == 3 and userput == 3:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nThat's a draw.")
    elif bot == 1 and userput == 2:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nYou win!")
        score = score + 1
    elif bot == 1 and userput == 3:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nBot wins!")
    elif bot == 2 and userput == 1:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nBot wins!")
    elif bot == 2 and userput == 3:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nYou win!")
        score = score + 1
    elif bot == 3 and userput == 1:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nYou win!")
        score = score + 1
    elif bot == 3 and userput == 2:
        print ("You:",userinput)
        print ("Bot:",botput)
        print ("\nBot wins!")
    else:                                                   #An impossible situation
        print ("I think I might have a mental breakdown.")
        break

    print ('''\nDo you wish to...
1. Play again.
2. Check your score.
3. Exit the game.
''')                                                    
    again = input("")
    
    if again.isdigit():                                     #Making sure the user's input is a digit
        print("")
    else:
        print ("You didn't enter a number.")
        break
    
    again = int(again)
    
    if again == 1:                                          #Looping if the user decides to play again
        print("")
    elif again == 2:
        print("You have won",score,"game(s) in",loop,"trials.\n")
    elif again == 3:
        break
    else:
        print ("You were supposed to enter either 1, 2 or 3.")
        break
