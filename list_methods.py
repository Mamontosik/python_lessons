friends = ['Максим', 'Леонид', 'Екатерина']
print(friends)
print('Количество друзей', len(friends))

friends.append('Роберт')
print(friends)
print('Количество друзей', len(friends))

print(friends.pop())
print(friends)
print('Осталось друзей', len(friends))

friends.clear()
print(friends)

friends = ['Максим', 'Леонид', 'Екатерина']
print(friends)

friends.remove('Леонид')
print(friends)

del friends[0]
print(friends )