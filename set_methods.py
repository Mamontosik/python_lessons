cities = {'Москва', 'Санкт-Петербург', 'Омск'}
print(type(cities))
print(cities)
cities.add('Будапешт')
print(cities)

cities.remove('Санкт-Петербург')
print(cities)

print(len(cities))

print('Москва' in cities)

print('new')
for city in cities:
    print(city)