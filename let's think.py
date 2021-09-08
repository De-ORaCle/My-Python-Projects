print("In this game we have three chances,let's go")
print("You will choose one option which is correct\n")
var = 0
wins = 0
while True:
    var += 1
    choice = input("Choose a number  in the range of 1-10:")
    if choice == "1":
        print("I am taken from a mine,and shut up in a wooden case,from which I am never releasedl,and yet I am used by almost every body. What am I?")
        print("a = rubber  b = gum  c = pencil lead  d = palm wine\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("correct\n")
              wins += 1
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")


    if choice == "2":
        print("As a stone inside a tree,I'll help your words out live thee. But if you push me as I stand, the more I movethe less I am. What am I?")
        print("a = pencil  b = coal  c = water  d = candle\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("correct\n")
              wins += 1
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("incorrect\n")
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")


    if choice == "3":
        print("Where there is light is the only place I can live,Yet if light shines on me I die. What am I?")
        print("a = night  b = day  c = mosquito  d = shadow\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("incorrect\n")
        elif ans == "d":
              print("correct\n")
              wins += 1
        else:
            print("wrong input\n")


    if choice == "4":
        print("I have a whole cities but no houses,forest but no tree, water but no fish. What am I?")
        print("a = globe  b = earth sketch  c = map  d = climate\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("correct\n")
              wins += 1
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")


    if choice == "5":
        print("What jump when it walk and sit?")
        print("a = lion  b = kangaroo  c = leopad  d = koala\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("correct\n")
              wins += 1
        elif ans == "c":
              print("incorrect\n")
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")

    if choice == "6":
        print("If you eat me,my sender will eat you")
        print("a = dog  b = fish hook  c = worms  d = book\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("correct\n")
              wins += 1
        elif ans == "c":
              print("incorrect\n")
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")

    if choice == "7":
        print("Forward am heavy backwards am not. What am I?")
        print("a = ton  b = drawer  c = car  d = shadow\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("correct\n")
              wins += 1
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("incorrect\n")
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")

    if choice == "8":
        print("I'am somthing beg people before I fly,what am I?")
        print("a = mosquito  b = rat  c = housefly  d = koala")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("correct\n")
              wins += 1
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")

    if choice == "9":
        print("I have a bed but I never sleep. I have mouth but I never speak?")
        print("a = river  b = deaf  c = dump  d = snail\n")
        ans = input("Choose an option: ")
        if ans == "a":
              print("correct\n")
              wins += 1
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("incorrect")
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")

    if choice == "10":
        print("I can be cracked and I can be played. I can be told and I can be made?")
        print("a = car  b = robot  c = joke  d = toy")
        ans = input("Choose an option: ")
        if ans == "a":
              print("incorrect\n")
        elif ans == "b":
              print("incorrect\n")
        elif ans == "c":
              print("correct\n")
              wins += 1
        elif ans == "d":
              print("incorrect\n")          
        else:
            print("wrong input\n")
    if var == 3:
        if wins == 3:
            print("You win")
        elif wins == 2:
            print("You tried")
        elif wins == 1:
            print("Try again later never give up")
        elif wins == 0:
            print("You lose")
        break
     


