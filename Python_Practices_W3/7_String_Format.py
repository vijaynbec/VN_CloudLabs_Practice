age = 36
#txt = "My name is John, I am " + age  #- it will error
# format string starts with f"              { }"

txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"  # :.2f reference to floating number/2 decimals
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#-------- Escape Character
txt = "We are the so-called 'Vikings' from the north."
print(txt)
txt = "We are the so-called \"Vikings\" from the north." # \ reference to escape character \"
print(txt)
txt = "We are the so-called \'Vikings\' from the north." # \ reference to escape character \'
print(txt)
txt = "We are the so-called \\'Vikings\\' from the north." # \ reference to escape character \\
print(txt)
txt = "We are the so-called Vikings\t from the north." # \ reference to escape character \t
print(txt)
txt = "We are the so-called Vikings\b from the north." # \ reference to escape character \b
print(txt)
txt = "We are the so-called Vikings\f from the north." # \ reference to escape character \b
print(txt)

x="1"
y=x.isascii()
print(y)





