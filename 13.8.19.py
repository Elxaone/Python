tickets = int(input("Введите количество необходимых билетов: "))
person = tickets

cost = 0
while person != 0:
    age_for_ticket = int(input('Укажите для какого возраста приобретается билет ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        cost += 990
        print('Стоимость билета: 990 руб.')
    else:
        cost += 1390
        print('Стоимость билета: 1390 руб.')
    person -= 1

if tickets > 3:
    sale = cost - ((cost / 100) * 10)
    print(f'Сумма к оплате {sale} руб., применена 10%-ая скидка за покупку более 3 билетов единовременно')
else:
    print(f'Сумма к оплате {cost} руб.')
