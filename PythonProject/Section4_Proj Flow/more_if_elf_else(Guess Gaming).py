ans=5
print("please guess the number between 1 to 10 ")
guess=int(input())

if guess < ans:
    print("please guess the higher")
    guess = int(input())
    if guess == ans:
        print("Hurry you guessed it correctly")
    else:
        print("Sorry try after sometime")
elif guess > ans:
    print("Please lower the guess")
    guess = int(input())
    if guess == ans:
        print("Hurry you guessed it correctly")
    else:
        print("Sorry try after sometime")
else:
    print("Congratulations you got first time")

##################Contidion Operators
<,>,>=,<=,==,!=

