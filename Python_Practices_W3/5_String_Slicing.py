print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#---- slicing string - find a part from string
b = "Hello, World!"
    #0123456789
    #       654321 (count as -ve number)
print(b[2:5])   #  (start at 2 end at 5 from R to L) - llo
print(b[2:])   #  (start at 2 end to till end,  R to L) - llo, World!
print(b[:4])   #  (start 0 to till 4th, R to L) - Hell
print('********')
#        "Hello, Wo r    l    d     !"
        -7-6-5     -4     -3   -2   -1
print(b[-2:])   #  (-2 reference to last two bytes till end of line)
print(b[:-4])   #  (start writing from R to L till -4) as Hello, Wo

