# На вход поступают две строки. Необходимо выяснить, является ли вторая строка подстрокой первой.

a = input ()
b = input ()
if b in a:
    print ('Да, является')
else:
    print ('Нет, не является')