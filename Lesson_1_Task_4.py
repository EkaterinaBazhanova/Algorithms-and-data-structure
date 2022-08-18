"""
Задача 4. Пользователь вводит две буквы.
 Определить, на каких местах алфавита они стоят,
 и сколько между ними находится букв.

 P.S. По условию пользователь идеален:
 вводит только буквы (только латинские или только русские)
 Важно: в таблице ASCII нет букв ё и Ё, вывод программы соответствующий
"""
print('Введите две буквы')
a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

a_ord = ord(a)
b_ord = ord(b)

if ord(a) < 192:
    first_pos = ord('a')
    a_pos = ord(a.lower()) - first_pos + 1
    b_pos = ord(b.lower()) - first_pos + 1

    print(f'Буква {a} стоит на месте {a_pos},')
    print(f'Буква {b} стоит на месте {b_pos},')

    if a_pos != b_pos:
        print(f'Количество букв между ними {abs(a_pos - b_pos) - 1}.')
    else:
        print(f'Количество букв между ними 0')
else:
    first_pos = ord('а')
    a_pos = ord(a.lower()) - first_pos + 1
    b_pos = ord(b.lower()) - first_pos + 1

    print(f'Буква {a} стоит на месте {a_pos},')
    print(f'Буква {b} стоит на месте {b_pos},')

    if a_pos != b_pos:
        print(f'Количество букв между ними {abs(a_pos - b_pos) - 1}.')
    else:
        print(f'Количество букв между ними 0')
