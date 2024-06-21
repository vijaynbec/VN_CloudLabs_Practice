# looks like list and it has two parts
vehicles ={
    'honda': 'honda 2000',
    'Nissan': 'nissan 5000',
    'chevy': 'chevy 7000',
    'maruti': 'maruti 15000',
    'tata': 'tata 8000',
    'audi': 'audi 4000'}
## format print into better way -> less efficient
# print("-" * 10 )
# for bet in vehicles:
#     print(bet,vehicles[bet], sep="->")

vehicles['BMW'] = 'c200BMW'
vehicles['Benz'] = 'C000B'
del vehicles['honda']  # method-1 to delete
vehicles.pop('tata')  # method 2 to delete entry
vehicles.pop('van', None)  # method 3 just pass if the key doesn't exist
## format print into better way -> more efficient  avoid extra memory overhead item()
# delete honda key
print("-" * 10)
for key, val in vehicles.items():
    print(key,val, sep=",  ")