print ("\n\nWelcome to the ABC Bank of Nigeria where we make banking as simple as ABC.")
input ("Press the \"Enter\" key to continue...\n\n")

#Welcome Message
'''The two lines above consists the welcome message'''


CustomerName1 = "Hillary Stone"
CustomerName2 = "Clement Johnson"
CustomerName3 = "Beatrice Shelby"
CustomerName4 = "Benjamin Christo"
CustomerName5 = "Candice Milton"
CustomerName6 = "Patrick Scott"
CustomerName7 = "Blessing Lionnel"
CustomerName8 = "Abraham Tammy"
CustomerName9 = "Dandelion Smith"
CustomerName0 = "Andrew Von Strucker"

UserAcctNumb1 = "3728748912"
UserAcctNumb2 = "5463756119"
UserAcctNumb3 = "6457834125"
UserAcctNumb4 = "3165106779"
UserAcctNumb5 = "2232574081"
UserAcctNumb6 = "2150046789"
UserAcctNumb7 = "7918706059"
UserAcctNumb8 = "4014600295"
UserAcctNumb9 = "5120781976"
UserAcctNumb0 = "3134602418"

UserPinNumb1 = "32519"
UserPinNumb2 = "59267"
UserPinNumb3 = "55410"
UserPinNumb4 = "15263"
UserPinNumb5 = "61980"
UserPinNumb6 = "16801"
UserPinNumb7 = "92001"
UserPinNumb8 = "51648"
UserPinNumb9 = "80197"
UserPinNumb0 = "20119"

CustomerAcctBal1 = 3020
CustomerAcctBal2 = 4105
CustomerAcctBal3 = 7030
CustomerAcctBal4 = 2560
CustomerAcctBal5 = 1765
CustomerAcctBal6 = 2315
CustomerAcctBal7 = 10040
CustomerAcctBal8 = 4000
CustomerAcctBal9 = 7180
CustomerAcctBal0 = 3560

#Customer's Data
'''This section stores data of Ten customers to be recalled later: Names, Account Number, Pin Numbers and Account Balance. Each piece of information is assigned to a variable'''


AcctNumber = input ("Enter your 10-digit account number:  ")
n = 2
while  n >= -1:
      n = n - 1
      if AcctNumber == UserAcctNumb1:
            print()
      elif AcctNumber == UserAcctNumb2:
            print()
      elif AcctNumber == UserAcctNumb3:
            print()
      elif AcctNumber == UserAcctNumb4:
            print()
      elif AcctNumber == UserAcctNumb5:
            print()
      elif AcctNumber == UserAcctNumb6:
            print()
      elif AcctNumber == UserAcctNumb7:
            print()
      elif AcctNumber == UserAcctNumb8:
            print()
      elif AcctNumber == UserAcctNumb9:
            print()
      elif AcctNumber == UserAcctNumb0:
            print()
      else:
            y = n + 1
            print ("Oops! You seem to have entered the wrong account number you have", y ,"more trials.\n")
            AcctNumber = input ("Enter your 10-digit account number:  ")
            if n == 0:
                  print ("\nDue to security reasons, you've been barred temporarily from using this service. \nThank you for choosing ABC Bank of Nigeria. Bye.")
                  exit()

#Account Number Verification
#If the account number entered by the user is not one of the registered numbers, the user tries again for three times till he/she gets it right.


PinNumber = input ("\n\nNow input your five digit PIN: ")
b = 2

while True:
      if AcctNumber == UserAcctNumb1 and PinNumber == UserPinNumb1:
            print("\n\nHi "+CustomerName1+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb2 and PinNumber == UserPinNumb2:
            print("\n\nHi "+CustomerName2+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb3 and PinNumber == UserPinNumb3:
            print("\n\nHi "+CustomerName3+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb4 and PinNumber == UserPinNumb4:
            print("\n\nHi "+CustomerName4+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb5 and PinNumber == UserPinNumb5:
            print("\n\nHi "+CustomerName5+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb6 and PinNumber == UserPinNumb6:
            print("\n\nHi "+CustomerName6+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb7 and PinNumber == UserPinNumb7:
            print("\n\nHi "+CustomerName7+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb8 and PinNumber == UserPinNumb8:
            print("\n\nHi "+CustomerName8+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb9 and PinNumber == UserPinNumb9:
            print("\n\nHi "+CustomerName9+", it's nice to have you back.\n What would you like to do today?")
            break
      elif AcctNumber == UserAcctNumb0 and PinNumber == UserPinNumb0:
            print("\n\nHi "+CustomerName0+", it's nice to have you back.\n What would you like to do today?")
            break
      else:
            b -= 1
            x = b + 1
            print ("Oops! You seem to have entered the wrong PIN number you have", x ,"more trials.\n")
            PinNumber = input ("\n\nNow input your five digit PIN: ")
            if b == 0:
                  print ("\nDue to security reasons, you've been barred temporarily from using this service. \nThank you for choosing ABC Bank of Nigeria. Bye.")
                  exit()

#Pin Verification
#If the user gets the account number right, he/she has three trials to try the correct pin else the program exits. If they get the pin right, they are greeted with a personalized welcome message.

while True:
      print ('''\nMain Menu
                              1 - View your balance
                              2 - Withdraw cash
                              3 - Deposit funds
                              4 - Exit''')
      choice = int(input ("Enter a choice:  "))

#Main Menu
#After a personalized greeting, the user has to make a choice as to what exactly they want to do.
                  
      if choice == 1:
            if AcctNumber == UserAcctNumb1:
                  CustomerAcctBal1 = str(CustomerAcctBal1)
                  print ("\n\n\nHey "+CustomerName1+", your account balance is N"+CustomerAcctBal1+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb2:
                  CustomerAcctBal2 = str(CustomerAcctBal2)
                  print ("\n\n\nHey "+CustomerName2+", your account balance is N"+CustomerAcctBal2+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb3:
                  CustomerAcctBal3 = str(CustomerAcctBal3)
                  print ("\n\n\nHey "+CustomerName3+", your account balance is N"+CustomerAcctBal3+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb4:
                  CustomerAcctBal4 = str(CustomerAcctBal4)
                  print ("\n\n\nHey "+CustomerName4+", your account balance is N"+CustomerAcctBal4+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb5:
                  CustomerAcctBal5 = str(CustomerAcctBal5)
                  print ("\n\n\nHey "+CustomerName5+", your account balance is N"+CustomerAcctBal5+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb6:
                  CustomerAcctBal6 = str(CustomerAcctBal6)
                  print ("\n\n\nHey "+CustomerName6+", your account balance is N"+CustomerAcctBal6+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb7:
                  CustomerAcctBal7 = str(CustomerAcctBal7)
                  print ("\n\n\nHey "+CustomerName7+", your account balance is N"+CustomerAcctBal7+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb8:
                  CustomerAcctBal8 = str(CustomerAcctBal8)
                  print ("\n\n\nHey "+CustomerName8+", your account balance is N"+CustomerAcctBal8+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb9:
                  CustomerAcctBal9 = str(CustomerAcctBal9)
                  print ("\n\n\nHey "+CustomerName9+", your account balance is N"+CustomerAcctBal9+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()
            elif AcctNumber == UserAcctNumb0:
                  CustomerAcctBal0 = str(CustomerAcctBal0)
                  print ("\n\n\nHey "+CustomerName0+", your account balance is N"+CustomerAcctBal0+"")
                  print ('''\nDo you wish to perform any other transactions?
                  1. Yes
                  2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()

#Checking The Balance
#If the user chooses to their balance, the code arranges their requested information (personalized) and displays it to them.

      elif choice == 2:
            print ('''Withdrawal Menu:
      1   -   N1000                           4   -    N10000
      2   -   N2000                           5   -    N20000
      3   -   N5000                           6   -    Cancel transaction''')
            withdraw = input ("Choose a withdrawal amount: ")
            if withdraw == "1":
                  ExitAmount = 1000
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int (CustomerAcctBal1)
                        FinalBalance1 = CustomerAcctBal1 - ExitAmount
                        if FinalBalance1 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance1 > 0:
                              FinalBalance1 = str(FinalBalance1)
                              print ("Withdrawal success! You have N"+FinalBalance1+" left in your account.")
                              CustomerAcctBal1 = FinalBalance1
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int (CustomerAcctBal2)
                        FinalBalance2 = CustomerAcctBal2 - ExitAmount
                        if FinalBalance2 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance2 > 0:
                              FinalBalance2 = str(FinalBalance2)
                              print ("Withdrawal success! You have N"+FinalBalance2+" left in your account.")
                              CustomerAcctBal2 = FinalBalance2
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int (CustomerAcctBal3)
                        FinalBalance3 = CustomerAcctBal3 - ExitAmount
                        if FinalBalance3 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance3 > 0:
                              FinalBalance3 = str(FinalBalance3)
                              print ("Withdrawal success! You have N"+FinalBalance3+" left in your account.")
                              CustomerAcctBal3 = FinalBalance3
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int (CustomerAcctBal4)
                        FinalBalance4 = CustomerAcctBal4 - ExitAmount
                        if FinalBalance4 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance4 > 0:
                              FinalBalance4 = str(FinalBalance4)
                              print ("Withdrawal success! You have N"+FinalBalance4+" left in your account.")
                              CustomerAcctBal4 = FinalBalance4
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int (CustomerAcctBal5)
                        FinalBalance5 = CustomerAcctBal5 - ExitAmount
                        if FinalBalance5 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance5 > 0:
                              FinalBalance5 = str(FinalBalance5)
                              print ("Withdrawal success! You have N"+FinalBalance5+" left in your account.")
                              CustomerAcctBal5 = FinalBalance5
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int (CustomerAcctBal6)
                        FinalBalance6 = CustomerAcctBal6 - ExitAmount
                        if FinalBalance6 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance6 > 0:
                              FinalBalance6 = str(FinalBalance6)
                              print ("Withdrawal success! You have N"+FinalBalance6+" left in your account.")
                              CustomerAcctBal6 = FinalBalance6
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int (CustomerAcctBal7)
                        FinalBalance7 = CustomerAcctBal7 - ExitAmount
                        if FinalBalance7 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance7 > 0:
                              FinalBalance7 = str(FinalBalance7)
                              print ("Withdrawal success! You have N"+FinalBalance7+" left in your account.")
                              CustomerAcctBal7 = FinalBalance7
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int (CustomerAcctBal8)
                        FinalBalance8 = CustomerAcctBal8 - ExitAmount
                        if FinalBalance8 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance8 > 0:
                              FinalBalance8 = str(FinalBalance8)
                              print ("Withdrawal success! You have N"+FinalBalance8+" left in your account.")
                              CustomerAcctBal8 = FinalBalance8
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int (CustomerAcctBal9)
                        FinalBalance9 = CustomerAcctBal9 - ExitAmount
                        if FinalBalance9 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance9 > 0:
                              FinalBalance9 = str(FinalBalance9)
                              print ("Withdrawal success! You have N"+FinalBalance9+" left in your account.")
                              CustomerAcctBal9 = FinalBalance9
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int (CustomerAcctBal0)
                        FinalBalance0 = CustomerAcctBal0 - ExitAmount
                        if FinalBalance0 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance0 > 0:
                              FinalBalance0 = str(FinalBalance0)
                              print ("Withdrawal success! You have N"+FinalBalance0+" left in your account.")
                              CustomerAcctBal0 = FinalBalance0
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()

            elif withdraw == "2":
                  ExitAmount = 2000
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int (CustomerAcctBal1)
                        FinalBalance1 = CustomerAcctBal1 - ExitAmount
                        if FinalBalance1 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance1 > 0:
                              FinalBalance1 = str(FinalBalance1)
                              print ("Withdrawal success! You have N"+FinalBalance1+" left in your account.")
                              CustomerAcctBal1 = FinalBalance1
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int (CustomerAcctBal2)
                        FinalBalance2 = CustomerAcctBal2 - ExitAmount
                        if FinalBalance2 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance2 > 0:
                              FinalBalance2 = str(FinalBalance2)
                              print ("Withdrawal success! You have N"+FinalBalance2+" left in your account.")
                              CustomerAcctBal2 = FinalBalance2
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int (CustomerAcctBal3)
                        FinalBalance3 = CustomerAcctBal3 - ExitAmount
                        if FinalBalance3 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance3 > 0:
                              FinalBalance3 = str(FinalBalance3)
                              print ("Withdrawal success! You have N"+FinalBalance3+" left in your account.")
                              CustomerAcctBal3 = FinalBalance3
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int (CustomerAcctBal4)
                        FinalBalance4 = CustomerAcctBal4 - ExitAmount
                        if FinalBalance4 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance4 > 0:
                              FinalBalance4 = str(FinalBalance4)
                              print ("Withdrawal success! You have N"+FinalBalance4+" left in your account.")
                              CustomerAcctBal4 = FinalBalance4
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int (CustomerAcctBal5)
                        FinalBalance5 = CustomerAcctBal5 - ExitAmount
                        if FinalBalance5 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance5 > 0:
                              FinalBalance5 = str(FinalBalance5)
                              print ("Withdrawal success! You have N"+FinalBalance5+" left in your account.")
                              CustomerAcctBal5 = FinalBalance5
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int (CustomerAcctBal6)
                        FinalBalance6 = CustomerAcctBal6 - ExitAmount
                        if FinalBalance6 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance6 > 0:
                              FinalBalance6 = str(FinalBalance6)
                              print ("Withdrawal success! You have N"+FinalBalance6+" left in your account.")
                              CustomerAcctBal6 = FinalBalance6
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int (CustomerAcctBal7)
                        FinalBalance7 = CustomerAcctBal7 - ExitAmount
                        if FinalBalance7 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance7 > 0:
                              FinalBalance7 = str(FinalBalance7)
                              print ("Withdrawal success! You have N"+FinalBalance7+" left in your account.")
                              CustomerAcctBal7 = FinalBalance7
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int (CustomerAcctBal8)
                        FinalBalance8 = CustomerAcctBal8 - ExitAmount
                        if FinalBalance8 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance8 > 0:
                              FinalBalance8 = str(FinalBalance8)
                              print ("Withdrawal success! You have N"+FinalBalance8+" left in your account.")
                              CustomerAcctBal8 = FinalBalance8
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int (CustomerAcctBal9)
                        FinalBalance9 = CustomerAcctBal9 - ExitAmount
                        if FinalBalance9 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance9 > 0:
                              FinalBalance9 = str(FinalBalance9)
                              print ("Withdrawal success! You have N"+FinalBalance9+" left in your account.")
                              CustomerAcctBal9 = FinalBalance9
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int (CustomerAcctBal0)
                        FinalBalance0 = CustomerAcctBal0 - ExitAmount
                        if FinalBalance0 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance0 > 0:
                              FinalBalance0 = str(FinalBalance0)
                              print ("Withdrawal success! You have N"+FinalBalance0+" left in your account.")
                              CustomerAcctBal0 = FinalBalance0
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                        
            elif withdraw == "3":
                  ExitAmount = 5000
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int (CustomerAcctBal1)
                        FinalBalance1 = CustomerAcctBal1 - ExitAmount
                        if FinalBalance1 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance1 > 0:
                              FinalBalance1 = str(FinalBalance1)
                              print ("Withdrawal success! You have N"+FinalBalance1+" left in your account.")
                              CustomerAcctBal1 = FinalBalance1
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int (CustomerAcctBal2)
                        FinalBalance2 = CustomerAcctBal2 - ExitAmount
                        if FinalBalance2 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance2 > 0:
                              FinalBalance2 = str(FinalBalance2)
                              print ("Withdrawal success! You have N"+FinalBalance2+" left in your account.")
                              CustomerAcctBal2 = FinalBalance2
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int (CustomerAcctBal3)
                        FinalBalance3 = CustomerAcctBal3 - ExitAmount
                        if FinalBalance3 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance3 > 0:
                              FinalBalance3 = str(FinalBalance3)
                              print ("Withdrawal success! You have N"+FinalBalance3+" left in your account.")
                              CustomerAcctBal3 = FinalBalance3
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int (CustomerAcctBal4)
                        FinalBalance4 = CustomerAcctBal4 - ExitAmount
                        if FinalBalance4 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance4 > 0:
                              FinalBalance4 = str(FinalBalance4)
                              print ("Withdrawal success! You have N"+FinalBalance4+" left in your account.")
                              CustomerAcctBal4 = FinalBalance4
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int (CustomerAcctBal5)
                        FinalBalance5 = CustomerAcctBal5 - ExitAmount
                        if FinalBalance5 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance5 > 0:
                              FinalBalance5 = str(FinalBalance5)
                              print ("Withdrawal success! You have N"+FinalBalance5+" left in your account.")
                              CustomerAcctBal5 = FinalBalance5
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int (CustomerAcctBal6)
                        FinalBalance6 = CustomerAcctBal6 - ExitAmount
                        if FinalBalance6 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance6 > 0:
                              FinalBalance6 = str(FinalBalance6)
                              print ("Withdrawal success! You have N"+FinalBalance6+" left in your account.")
                              CustomerAcctBal6 = FinalBalance6
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int (CustomerAcctBal7)
                        FinalBalance7 = CustomerAcctBal7 - ExitAmount
                        if FinalBalance7 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance7 > 0:
                              FinalBalance7 = str(FinalBalance7)
                              print ("Withdrawal success! You have N"+FinalBalance7+" left in your account.")
                              CustomerAcctBal7 = FinalBalance7
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int (CustomerAcctBal8)
                        FinalBalance8 = CustomerAcctBal8 - ExitAmount
                        if FinalBalance8 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance8 > 0:
                              FinalBalance8 = str(FinalBalance8)
                              print ("Withdrawal success! You have N"+FinalBalance8+" left in your account.")
                              CustomerAcctBal8 = FinalBalance8
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int (CustomerAcctBal9)
                        FinalBalance9 = CustomerAcctBal9 - ExitAmount
                        if FinalBalance9 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance9 > 0:
                              FinalBalance9 = str(FinalBalance9)
                              print ("Withdrawal success! You have N"+FinalBalance9+" left in your account.")
                              CustomerAcctBal9 = FinalBalance9
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int (CustomerAcctBal0)
                        FinalBalance0 = CustomerAcctBal0 - ExitAmount
                        if FinalBalance0 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance0 > 0:
                              FinalBalance0 = str(FinalBalance0)
                              print ("Withdrawal success! You have N"+FinalBalance0+" left in your account.")
                              CustomerAcctBal0 = FinalBalance0
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()

            elif withdraw == "4":
                  ExitAmount = 10000
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int (CustomerAcctBal1)
                        FinalBalance1 = CustomerAcctBal1 - ExitAmount
                        if FinalBalance1 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance1 > 0:
                              FinalBalance1 = str(FinalBalance1)
                              print ("Withdrawal success! You have N"+FinalBalance1+" left in your account.")
                              CustomerAcctBal1 = FinalBalance1
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int (CustomerAcctBal2)
                        FinalBalance2 = CustomerAcctBal2 - ExitAmount
                        if FinalBalance2 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance2 > 0:
                              FinalBalance2 = str(FinalBalance2)
                              print ("Withdrawal success! You have N"+FinalBalance2+" left in your account.")
                              CustomerAcctBal2 = FinalBalance2
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int (CustomerAcctBal3)
                        FinalBalance3 = CustomerAcctBal3 - ExitAmount
                        if FinalBalance3 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance3 > 0:
                              FinalBalance3 = str(FinalBalance3)
                              print ("Withdrawal success! You have N"+FinalBalance3+" left in your account.")
                              CustomerAcctBal3 = FinalBalance3
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int (CustomerAcctBal4)
                        FinalBalance4 = CustomerAcctBal4 - ExitAmount
                        if FinalBalance4 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance4 > 0:
                              FinalBalance4 = str(FinalBalance4)
                              print ("Withdrawal success! You have N"+FinalBalance4+" left in your account.")
                              CustomerAcctBal4 = FinalBalance4
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int (CustomerAcctBal5)
                        FinalBalance5 = CustomerAcctBal5 - ExitAmount
                        if FinalBalance5 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance5 > 0:
                              FinalBalance5 = str(FinalBalance5)
                              print ("Withdrawal success! You have N"+FinalBalance5+" left in your account.")
                              CustomerAcctBal5 = FinalBalance5
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int (CustomerAcctBal6)
                        FinalBalance6 = CustomerAcctBal6 - ExitAmount
                        if FinalBalance6 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance6 > 0:
                              FinalBalance6 = str(FinalBalance6)
                              print ("Withdrawal success! You have N"+FinalBalance6+" left in your account.")
                              CustomerAcctBal6 = FinalBalance6
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int (CustomerAcctBal7)
                        FinalBalance7 = CustomerAcctBal7 - ExitAmount
                        if FinalBalance7 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance7 > 0:
                              FinalBalance7 = str(FinalBalance7)
                              print ("Withdrawal success! You have N"+FinalBalance7+" left in your account.")
                              CustomerAcctBal7 = FinalBalance7
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int (CustomerAcctBal8)
                        FinalBalance8 = CustomerAcctBal8 - ExitAmount
                        if FinalBalance8 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance8 > 0:
                              FinalBalance8 = str(FinalBalance8)
                              print ("Withdrawal success! You have N"+FinalBalance8+" left in your account.")
                              CustomerAcctBal8 = FinalBalance8
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int (CustomerAcctBal9)
                        FinalBalance9 = CustomerAcctBal9 - ExitAmount
                        if FinalBalance9 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance9 > 0:
                              FinalBalance9 = str(FinalBalance9)
                              print ("Withdrawal success! You have N"+FinalBalance9+" left in your account.")
                              CustomerAcctBal9 = FinalBalance9
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int (CustomerAcctBal0)
                        FinalBalance0 = CustomerAcctBal0 - ExitAmount
                        if FinalBalance0 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance0 > 0:
                              FinalBalance0 = str(FinalBalance0)
                              print ("Withdrawal success! You have N"+FinalBalance0+" left in your account.")
                              CustomerAcctBal0 = FinalBalance0
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()

            elif withdraw == "5":
                  ExitAmount = 20000
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int (CustomerAcctBal1)
                        FinalBalance1 = CustomerAcctBal1 - ExitAmount
                        if FinalBalance1 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance1 > 0:
                              FinalBalance1 = str(FinalBalance1)
                              print ("Withdrawal success! You have N"+FinalBalance1+" left in your account.")
                              CustomerAcctBal1 = FinalBalance1
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int (CustomerAcctBal2)
                        FinalBalance2 = CustomerAcctBal2 - ExitAmount
                        if FinalBalance2 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance2 > 0:
                              FinalBalance2 = str(FinalBalance2)
                              print ("Withdrawal success! You have N"+FinalBalance2+" left in your account.")
                              CustomerAcctBal2 = FinalBalance2
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int (CustomerAcctBal3)
                        FinalBalance3 = CustomerAcctBal3 - ExitAmount
                        if FinalBalance3 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance3 > 0:
                              FinalBalance3 = str(FinalBalance3)
                              print ("Withdrawal success! You have N"+FinalBalance3+" left in your account.")
                              CustomerAcctBal3 = FinalBalance3
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int (CustomerAcctBal4)
                        FinalBalance4 = CustomerAcctBal4 - ExitAmount
                        if FinalBalance4 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance4 > 0:
                              FinalBalance4 = str(FinalBalance4)
                              print ("Withdrawal success! You have N"+FinalBalance4+" left in your account.")
                              CustomerAcctBal4 = FinalBalance4
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int (CustomerAcctBal5)
                        FinalBalance5 = CustomerAcctBal5 - ExitAmount
                        if FinalBalance5 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance5 > 0:
                              FinalBalance5 = str(FinalBalance5)
                              print ("Withdrawal success! You have N"+FinalBalance5+" left in your account.")
                              CustomerAcctBal5 = FinalBalance5
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int (CustomerAcctBal6)
                        FinalBalance6 = CustomerAcctBal6 - ExitAmount
                        if FinalBalance6 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance6 > 0:
                              FinalBalance6 = str(FinalBalance6)
                              print ("Withdrawal success! You have N"+FinalBalance6+" left in your account.")
                              CustomerAcctBal6 = FinalBalance6
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int (CustomerAcctBal7)
                        FinalBalance7 = CustomerAcctBal7 - ExitAmount
                        if FinalBalance7 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance7 > 0:
                              FinalBalance7 = str(FinalBalance7)
                              print ("Withdrawal success! You have N"+FinalBalance7+" left in your account.")
                              CustomerAcctBal7 = FinalBalance7
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int (CustomerAcctBal8)
                        FinalBalance8 = CustomerAcctBal8 - ExitAmount
                        if FinalBalance8 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance8 > 0:
                              FinalBalance8 = str(FinalBalance8)
                              print ("Withdrawal success! You have N"+FinalBalance8+" left in your account.")
                              CustomerAcctBal8 = FinalBalance8
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int (CustomerAcctBal9)
                        FinalBalance9 = CustomerAcctBal9 - ExitAmount
                        if FinalBalance9 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance9 > 0:
                              FinalBalance9 = str(FinalBalance9)
                              print ("Withdrawal success! You have N"+FinalBalance9+" left in your account.")
                              CustomerAcctBal9 = FinalBalance9
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int (CustomerAcctBal0)
                        FinalBalance0 = CustomerAcctBal0 - ExitAmount
                        if FinalBalance0 < 0:
                              print ("We are sorry. You have insufficient balance to complete this transaction.")
                        elif FinalBalance0 > 0:
                              FinalBalance0 = str(FinalBalance0)
                              print ("Withdrawal success! You have N"+FinalBalance0+" left in your account.")
                              CustomerAcctBal0 = FinalBalance0
                        print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                        Append = input ("Enter 1 or 2:  ")
                        if Append == "1":
                              print()
                        elif Append == "2":
                              print ("\nThank you for banking with us.")
                              exit()
                        else:
                              print ("You must have entered a wrong input. Thank you for banking with us.")
                              exit()

            elif withdraw == "6":
                  print ('''Withdrawal Transaction Cancelled
      No amount deducted.''')
                  print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("You must have entered a wrong input. Thank you for banking with us.")
                        exit()

#Withdrawal Option
#A series of subtraction operations make the above code functional. Subtracting the amount to be withdrawed from the present balance. If the amount to be withdrawed is greater than the account balance, the user is notified.

      elif choice == 3:
            print ('''Deposit Menu:
      (You can only deposit in currency denominations of N500 and N1000)

      In what denomination do you want to perform this transaction?
         1.   N500
         2.   N1000''')
            denomination = input ("\nEnter either 1 or 2:   ")
            if denomination == "1":
                  print ("\nHow many N500 notes do you want to deposit? (Minimum of 1; Maximum of 10 at a time)")
                  denNumb = input ("Enter between 1-10:  ")
                  if denNumb.isdigit() is True:
                        print()
                  else:
                        print("\nError. Enter a valid number.")
                        break
                  denNumb = int(denNumb)
                  if denNumb > 10:
                        print ("\nError. You cannot enter more than 10 denominations.")
                        break
                  Deposit = denNumb * 500
                  Deposit = str(Deposit)
                  print ("You're about to deposit N"+Deposit+" into your account. Press \"Enter\" to continue.")
                  input()
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int(CustomerAcctBal1) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal1 = str(CustomerAcctBal1)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal1+".")
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int(CustomerAcctBal2) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal2 = str(CustomerAcctBal2)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal2+".")
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int(CustomerAcctBal3) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal3 = str(CustomerAcctBal3)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal3+".")
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int(CustomerAcctBal4) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal4 = str(CustomerAcctBal4)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal4+".")
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int(CustomerAcctBal5) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal5 = str(CustomerAcctBal5)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal5+".")
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int(CustomerAcctBal6) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal6 = str(CustomerAcctBal6)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal6+".")
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int(CustomerAcctBal7) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal7 = str(CustomerAcctBal7)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal7+".")
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int(CustomerAcctBal8) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal8 = str(CustomerAcctBal8)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal8+".")
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int(CustomerAcctBal9) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal9 = str(CustomerAcctBal9)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal9+".")
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int(CustomerAcctBal0) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal0 = str(CustomerAcctBal0)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal0+".")
                  print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("\nYou seem to have entered a wrong option.\nThank you for banking with us. ")
                        exit()
            elif denomination == "2":
                  print ("\nHow many N1000 notes do you want to deposit? (Minimum of 1; Maximum of 10 at a time)")
                  denNumb = input ("Enter between 1-10:  ")
                  if denNumb.isdigit() is True:
                        print()
                  else:
                        print("\nError. Enter a valid number.")
                        break
                  denNumb = int(denNumb)
                  if denNumb > 10:
                        print ("\nError. You cannot enter more than 10 denominations.")
                        break
                  Deposit = denNumb * 1000
                  Deposit = str(Deposit)
                  print ("You're about to deposit N"+Deposit+" into your account. Press \"Enter\" to continue.")
                  input()
                  print ("\nHow many N1000 notes do you want to deposit? (Minimum of 1; Maximum of 10 at a time)")
                  denNumb = input ("Enter between 1-10:  ")
                  if AcctNumber == UserAcctNumb1:
                        CustomerAcctBal1 = int(CustomerAcctBal1) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal1 = str(CustomerAcctBal1)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal1+".")
                  elif AcctNumber == UserAcctNumb2:
                        CustomerAcctBal2 = int(CustomerAcctBal2) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal2 = str(CustomerAcctBal2)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal2+".")
                  elif AcctNumber == UserAcctNumb3:
                        CustomerAcctBal3 = int(CustomerAcctBal3) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal3 = str(CustomerAcctBal3)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal3+".")
                  elif AcctNumber == UserAcctNumb4:
                        CustomerAcctBal4 = int(CustomerAcctBal4) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal4 = str(CustomerAcctBal4)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal4+".")
                  elif AcctNumber == UserAcctNumb5:
                        CustomerAcctBal5 = int(CustomerAcctBal5) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal5 = str(CustomerAcctBal5)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal5+".")
                  elif AcctNumber == UserAcctNumb6:
                        CustomerAcctBal6 = int(CustomerAcctBal6) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal6 = str(CustomerAcctBal6)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal6+".")
                  elif AcctNumber == UserAcctNumb7:
                        CustomerAcctBal7 = int(CustomerAcctBal7) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal7 = str(CustomerAcctBal7)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal7+".")
                  elif AcctNumber == UserAcctNumb8:
                        CustomerAcctBal8 = int(CustomerAcctBal8) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal8 = str(CustomerAcctBal8)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal8+".")
                  elif AcctNumber == UserAcctNumb9:
                        CustomerAcctBal9 = int(CustomerAcctBal9) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal9 = str(CustomerAcctBal9)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal9+".")
                  elif AcctNumber == UserAcctNumb0:
                        CustomerAcctBal0 = int(CustomerAcctBal0) + int(Deposit)
                        Deposit = str(Deposit)
                        CustomerAcctBal0 = str(CustomerAcctBal0)
                        print ("Sucess! You've added N"+Deposit+" to your account balance. Your new balance is N"+CustomerAcctBal0+".")
                  print ('''\nDo you wish to perform any other transactions?
            1. Yes
            2. No ''')
                  Append = input ("Enter 1 or 2:  ")
                  if Append == "1":
                        print()
                  elif Append == "2":
                        print ("\nThank you for banking with us.")
                        exit()
                  else:
                        print ("\nYou seem to have entered a wrong option.\nThank you for banking with us. ")
                        exit()

#Deposit Option
#Similar to the withdrawal option, the deposit option functions due to addition operators. Moreover, the user is limited to only depositing two denominatons and not more than 10 notes at a time.

      elif choice == 4:
            print ('''Are you sure you want to exit:
      1.  Yes
      2.  No ''')
            exitChoice = input("Enter either 1 or 2:  ")
            if exitChoice == "1":
                  exit()
            elif exitChoice == "2":
                  print ("\nWe go again!")
            else:
                  print ("You did not enter a valid option. For security purposes, you will have to restart if  you wish.")
                  exit()

#Exit Option
#The choice to exit the program is functional due to the above code.

else:
      print ("You did not enter a valid option. Sorry, try again.")
      
#If you loved this or you're looking for more of this, check https://github.com/De-ORaCle
#Don't forget to follow me.
