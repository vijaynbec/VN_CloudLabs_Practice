import random
high=10
ans=random.randint(1,high)
print(ans)  # just added to test
guess= 0 # initialize
print("please guess the number between 1 to {} ".format(high))

while guess != ans:
    guess=int(input())
# for loop usage
    if guess == ans:
       print("Hurry you guessed it correctly")
       break
    else:
        if guess > ans:
           print("Please lower the guess")
        else:
           print("Please higher the guess")

