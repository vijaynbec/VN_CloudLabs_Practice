# def is_palindrom(string):
#     # backwards = string[::-1]
#     # return backwards == string
# # above two lines also return like below
#       return string[::-1].casefold() == string.casefold()
#     # casefold is to cover the upper case of the sentence
# text = input("please enter the word: ")
# if is_palindrom(text):
#     print ("text  {} is palindrome".format(text))
# else:
#     print("text  {} is not palindrome".format(text))
#

def sume_eo(n, t):
    if t == 'e':
        begin = 2
    elif t == 'o':
        begin = 1
    else:
        return -1
    return (sum(range(begin, n, 2)))


x = sume_eo(10, 'o')
y = sume_eo(10, 'e')
print(x)
print(y)