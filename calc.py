'''input - оператор пользовательского ввода
используем float, чтобы не произошла конкатенация строк
используем str для перевода числа в строковое значение'''

what = input('Что делаем? (+, -): ')

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))

if what == '+':
    c = a + b
    print('Результат: ' + str(c)) 
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
else:
    print('Выбрана неверная операция')


