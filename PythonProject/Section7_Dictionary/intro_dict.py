
# looks like list and it has two parts
vehicles ={
    'honda': 'honda 2000',
    'Nissan': 'nissan 5000',
    'chey': 'chevy 7000',
    'maruti': 'maruti 15000',
    'tata': 'tata 8000',
    'audi': 'audi 4000'
}
# key to index  (
my_car = vehicles['audi']
print(my_car)

comuter = vehicles['tata']
print(comuter)

# get method
milage = vehicles.get('honda')
print(milage)
# case sensitive
milage1 = vehicles.get('Honda')
print(milage1)

# throw error by index method if values are incorrect
comuter1 = vehicles['Tata']
print(comuter1)
