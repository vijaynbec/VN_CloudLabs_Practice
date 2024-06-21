##Binary search
low=1
high=500
print("please think of number between {} and {}".format(low,high))
print("Guess the number to start")
guess=1
while True:
    guess = low + (high-low) // 2
    high_low = input("My guess is {}. Should I guess low or high number ? "
                     "Enter h or l or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
        # guess higher
        low = guess + 1
    if high_low == "l":
        # guess lower
        high = guess - 1
    elif high_low == "c":
        print("I got it in {}".format(guess))
    else:
        print("please enter h,l or c")
    guess=guess+1

number = 5
multiplier = 8
answer = 0

# add your loop after this comment

for i in range(multiplier):
    answer += number
print(answer)