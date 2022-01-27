friend_name = 'Максим'
friends = ['Максим', 'Леонид', 'Петр']
roles = ['admin', 'guest', 'user']

#Проверка список
if 'Максим' in friends:
    print('Я знаю этого человека, он мой друг')

if 'М' in friend_name:
    print('Буква М есть в имени друга')

#while
print('Цикл while')
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i+=1

#for
print('Цикл FOR')
for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)

for role in roles:
    print(role)

print('Завершаем работу программы')
