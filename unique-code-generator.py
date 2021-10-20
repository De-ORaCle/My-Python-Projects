import random

figure1 = random.randint(0,9)
figure2 = random.randint(0,9)
figure3 = random.randint(0,9)
figure4 = random.randint(0,9)
figure5 = random.randint(0,9)
figure6 = random.randint(0,9)
figure7 = random.randint(0,9)
figure8 = random.randint(0,9)

figure1 = str(figure1)
figure2 = str(figure2)
figure3 = str(figure3)
figure4 = str(figure4)
figure5 = str(figure5)
figure6 = str(figure6)
figure7 = str(figure7)
figure8 = str(figure8)


if figure2 == "0":
    figure2 = "b"
elif figure2 == "1":
    figure2 = "g"
elif figure2 == "2":
    figure2 = "k"
elif figure2 == "3":
    figure2 = "p"
elif figure2 == "4":
    figure2 = "w"
elif figure2 == "5":
    figure2 = "h"
elif figure2 == "6":
    figure2 = "t"
elif figure2 == "7":
    figure2 = "y"
elif figure2 == "8":
    figure2 = "c"
elif figure2 == "9":
    figure2 = "j"


if figure7 == "0":
    figure7 = "a"
elif figure7 == "1":
    figure7 = "r"
elif figure7 == "2":
    figure7 = "b"
elif figure7 == "3":
    figure7 = "h"
elif figure7 == "4":
    figure7 = "q"
elif figure7 == "5":
    figure7 = "k"
elif figure7 == "6":
    figure7 = "e"
elif figure7 == "7":
    figure7 = "a"
elif figure7 == "8":
    figure7 = "f"
elif figure7 == "9":
    figure7 = "x"


print (figure1+figure2+figure3+figure4+figure5+figure6+figure7)
