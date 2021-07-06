n = 18
C = 1
print("!!!!!!!!! Welcome to our all new 'GUESSING THE RIGHT ONE' Game !!!!!!!!! \n Max chances (6)\n")

while (C <=6):
    x = int(input("Please write the number here which you think is correct! \n--> "))

    if 15 < x < n:
        print("Nopes ! You are just some steps less from guessing the correct ")
    elif x < 15:
        print("NOOOO !!, You are too less from the correct number")
    elif 21 > x > n:
        print("Nopes ! You are just some steps more from guession the correct ")
    elif x == 21:
        print("Nopes ! You are just some steps more from guession the correct ")
    elif x > 21:
        print("NOOOO !!, You are too more from the correct number")
    elif x == 15:
        print("Nopes ! You are just some steps less from guessing the correct ")
    else:
        print("Yeah !!!, You Won the game \n")
        print("No. of gueses you tooks - ", C )
        break
    print(6-C, "no. of guesses left")
    C = C +1

    if (C>6):
        print("YOU LOOSE \n !!! GAME OVER !!!")
