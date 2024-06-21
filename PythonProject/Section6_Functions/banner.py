# helps in formating a text by functions
import random


def banner(text):
    screen_size = 80
    if len(text) > screen_size-2:
        print("Noo!!")
    if text == "*":
        print(text * screen_size)
    else:
        center_it = text.center(screen_size)
        out_string = "**{0}**".format(center_it)
        print(out_string)

banner("*")
banner("Hi I am writing to display this banner")
banner(" ")
# function not return anything
result = banner("passingtext")
print(result)

print("*" * 90)
def banner_arg(text, screen_size):
    screen_size = 80
    if len(text) > screen_size-2:
        print("Noo!!")
    if text == "*":
        print(text * screen_size)
    else:
        center_it = text.center(screen_size)
        out_string = "**{0}**".format(center_it)
        print(out_string)

banner_arg("*", 66)
banner_arg("Hi I am writing to display this banner", 66)
banner_arg(" ", 66)
# function not return anything
result = banner_arg("passingtext", 66)
print(result)

print("*" * 90)
def banner_arg(text, screen_size = 66):
    screen_size = 80
    if len(text) > screen_size-2:
        print("Noo!!")
    if text == "*":
        print(text * screen_size)
    else:
        center_it = text.center(screen_size)
        out_string = "**{0}**".format(center_it)
        print(out_string)

banner_arg("*")
banner_arg("Hi I am writing to display this banner")
banner_arg(" ")
# function not return anything
result = banner_arg("passingtext")
print(result)