# Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“.
#  Необходимо определить и вывести пол человека, которому данное письмо адресовано. 
# Приглашение письма запрашивается у пользователя.

a = input().split()
if a[1] == 'Mr.':
    print ('Пол: мужской')
else:
    print ('Пол: женский')
