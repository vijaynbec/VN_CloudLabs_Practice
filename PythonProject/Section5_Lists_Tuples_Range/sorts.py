light = " Printing the foot steps in others life"
letsort = sorted(light)  # sort capital letters then small letters
print(letsort)

numbers= [5, 78, 23, 8, .05, 15, 88, 1]
dosort = sorted(numbers)
print(dosort)
print(numbers)
numbers.sort()   # .sort is applicale only for list not for tuples
print(numbers)

sort_light=sorted("Printing the foot steps in others life",key=str.casefold)
sort_lightno=sorted("Printing the foot steps in others life")
print((sort_light))  # sort all letters in order irrespective of small/capitals
print((sort_lightno))  # sort capital letters then small letters

names=["rajesh", "Nag","vij","pal","Singh","patel","joshi"]
names.sort()
print(names)
names.sort(key=str.casefold)
print((names))