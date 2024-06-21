# looks like list and it has two parts
vehicles ={
    'honda': 'honda 2000',
    'Nissan': 'nissan 5000',
    'chevy': 'chevy 7000',
    'maruti': 'maruti 15000',
    'tata': 'tata 8000',
    'audi': 'audi 4000',
    'chevy': 'New insertiion for same chevy'  # New chevy
}
## format print into better way -> less efficient
# print("-" * 10 )
# for bet in vehicles:
#     print(bet,vehicles[bet], sep="->")

vehicles['BMW'] = 'c200BMW'
vehicles['Benz'] = 'C000B'
vehicles['tata'] = "Ferrari"  # Change tata as Ferrari
vehicles['honda']= 'Accord' # Change tata as Ferrari

# last values get replaced for Chevy
for key, value in vehicles.items():
    print(key,value, sep=" ---> ")