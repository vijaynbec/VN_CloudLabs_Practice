# looks like list and it has two parts
vehicles ={
    'honda': 'honda 2000',
    'Nissan': 'nissan 5000',
    'chey': 'chevy 7000',
    'maruti': 'maruti 15000',
    'tata': 'tata 8000',
    'audi': 'audi 4000'
}

for key in vehicles:
    print(key)
print("-" * 10 )
for keyval in vehicles:
    print(keyval, vehicles[keyval])
## format print into better way -> less efficient
print("-" * 10 )
for bet in vehicles:
    print(bet,vehicles[bet], sep="->")

## format print into better way -> more efficient  avoid extra memory overhead item()
print("-" * 10)
for key, val in vehicles.items():
    print(key,val, sep=",  ")