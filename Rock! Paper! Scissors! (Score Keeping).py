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
