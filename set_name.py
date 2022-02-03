print('Собираемся в отпуск')
max_things = {'Телефон', 'Зубная щетка', 'Носки', 'Штаны', 'Бритва', 'Рубашка'}
kate_tings = {'Платье', 'Телефон', 'Носки', 'Помада', 'Зонтик', 'Зубная щетка'}

#какие вещи взяли оба супруга
print(max_things | kate_tings)

#отличные друг от друга вещи
print(max_things & kate_tings)

#какие вещи взял только Макс
print(max_things - kate_tings)

#какие вещи взяла только Катя
print(kate_tings - max_things)

