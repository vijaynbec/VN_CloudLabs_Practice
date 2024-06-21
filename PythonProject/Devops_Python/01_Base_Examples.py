# String concotan
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)
# length of string
text = "Python is awesome"
length = len(text)
print('*' * 80)
print("Length of the string:", length)   # other way
print(len(text))   # second way
# upper case/lower case
print('*' * 80)
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print(text.upper())
print(text.lower())
# replace the string
print('*' * 80)
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified by great(replace):", new_text)
print(text.replace('Python', 'Python with AWS'))
# split the words
print('*' * 80)
text = "Python is awesome"
words = text.split()
print("Words:", words)
print(text.split())
# text strip
print('*' * 80)
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
print(text.strip())
# Float variables
# Float variables
print('*' * 80)
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
print("-------- Basic Arithmetics ------- ")
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)


# Integer variables
num1 = 10
num2 = 5
print('*' * 80)

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

print('*' * 80)


import re

text = "The quick brown fox"
pattern = r"brown"
#print(text)
print("*****search for brown 'import re' ******** ")
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
########

print("*****replacement for brown to red 'import re' ******** ")

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)


print("*****search for brown to red 'import re' ******** ")
text = "The quick brown fox"
check = r"brown"

search = re.search(check, text)
if search:
    print("check search found:", search.group())
else:
    print("check search not found")

#################split
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)






