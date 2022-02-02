friends = ['Петр', 'Иван', 'Семен']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

#Добавляем возраст другу

friend = {
    'name': 'Максим',
    'age': 31,
    'car': 'yes'
}

print(friend)
print(type(friend))

print(friend['age'])

friend['are_married'] = True
print(friend)
friend['are_married'] = False
print(friend)

del friend['age']
print(friend)

if 'age' in friend:
    print('Есть возраст')

if 'name' in friend:
    print('Имя в паспорте есть')