# Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта. 
# При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции. 
# Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена ошибка неправильной операции. 
# Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
# Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
# При строчных операциях необходимо вывести детальную информацию по лифту:
# наименование, количество поднятий и процент от общего количества поднятий всех лифтов. 
from Classes.Class_for_Task0 import Elevator

lift1 = Elevator(name = 'lift1')
lift1.up(3)
lift1.lift (5)
lift1.up (3)
lift1.down(5)
lift1.up(6)
lift1.down(3)
lift1.up(2)

lift2 = Elevator(name = 'lift2')
lift2.up(3)
lift2.up (3)
lift2.down(5)
lift2.up(6)
lift2.down(3)

lift3 = Elevator(name = 'lift3')
lift3.up(3)

print(Elevator.info(lift1, lift2,lift3))             # название, количество поднятий и их процент на долю лифта
print(Elevator.larger_up(lift1,lift2,lift3))         # лифт, который совершил большее количество поднятий
decorator = Elevator.decor(Elevator.sum_up)
print(decorator(lift1,lift2,lift3))                  # общее количество поднятий всех лифтов (с использованием декоратора)
print (lift1+lift2-lift3)                            # операция сложения/вычитания


