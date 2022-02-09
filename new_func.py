#модуль числа
print(abs(-7))

#min, max
numbers = [5,15,7,1,-9,0]
print(max(numbers))
print(min(numbers))

#round
print(round(10.9872, 1))

#sum
print(sum(numbers))

#enumerate
winners = ['Леонид', 'Максим', 'Екатерина']
for number, winner in enumerate(winners, 1):
    print(number, winner)