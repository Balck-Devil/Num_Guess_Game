import random

ON=random.randint(1,100)


while True:
    guess=int(input("Enter The Num You Guess Between 1 TO 99 :- "))

    if ON < guess :
        print("Number Is Too Big...")

    elif ON > guess :
        print("Number Is Too Short...")

    else:
        print("Congrats You Won The Game !!!")
        break