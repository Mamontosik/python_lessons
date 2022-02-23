gloval_var = 2

def my_f():
    result = gloval_var ** 5
    print(result)

def my_change_f():
    global global_var
    global_var = 'Какая-то строка'

my_f()