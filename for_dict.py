friend = {
    'name': 'Максим',
    'age': '31',
    'has_car': True
}

print('new')
#перебор по ключам
for key in friend.keys():
    print(friend)
    print(type(friend[key]))

for key in friend:
    print(friend)
    print(type(friend[key ]))

print('new')
#по значениям
for val in friend.values():
    print(friend)
    print(type(friend))

print('new')
#пары ключ значение
for item in friend.items():
    print(item)

print('new')
for key, val in friend.items():
    print(key)
    print(val)