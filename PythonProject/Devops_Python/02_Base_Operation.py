print('*' * 80)
num1 = 5
num2 = 2

# Basic Arithmetic
print("-------- Basic Arithmetics ------- ")
print(num1,num2)
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)
# Basic comparisons
print("-------- Basic comparisons <, >, <=, >=, ==, and != ------- ")
print(num1,num2)

less_than = num1 < num2
print("less than num1 < num2:", less_than)

great_than = num1 > num2
print("great num1 > num2:", great_than)

lesseq_than = num1 <= num2
print("lesseq than num1 <= num2:", lesseq_than)

greateq_than = num1 >= num2
print("greateq num1 >= num2:", greateq_than)

eq_than = num1 == num2
print("eq num1 == num2:", eq_than)

noteq_than = num1 != num2
print("noteq num1 != num2:", noteq_than)

# Logical Operators
print("-------- Logical Operators  and, or, not ------- ")
x = True
y = False
print(x,y)
and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result)
print("x or y:", or_result)
print("not x:", not_result_x)
print("not y:", not_result_y)

# Assignment Operators
print("-------- Assignment Operators  (+=, -=, *=, /=) ------- ")
total = 10
print(total)
total += 5  # add 5  = 15
print("+= 5 total:", total)
total -= 3  # deduct 3 = 7
print("-= 3 total:", total)
total *= 2 # multiply 2 = 20
print("*2 total:", total)
total /= 4  # division 4 = 2.5
print("/4 total:", total)

print("Final total:", total)

# Identity and Membership Operators
my_list = [1,2,3,4,5]
a=my_list
b=[1,2,3,4,5]

is_object = a is my_list
print(is_object)
isnot_object = a is not my_list
print(isnot_object)

print("Membership operators in and not_in")
in_object = a in my_list
print(in_object)
notin_object = a not in my_list
print(notin_object)

