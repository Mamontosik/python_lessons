print('Соревнования по PYTHON!')
count = int(input('Введите количество участников соревнования: '))

i = count
members = []
while i > 0:
    name = input('Кто занял {} место на соревновании: '.format(i))
    members.append(name)
    i-=1

#Кто участвовал в соревнованиях
print('В соревнованиях участвовали:', members)

#Разворачиваем список
members.reverse()

#Выводим результат
result = members[:3]

result = 'Победители: {}. Поздравляем '.format(result)
print(result)
