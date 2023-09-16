#2
p = int(input("Показатель степени: "))
n = int(input("Предел: "))

i = 1
while i ** p <= n:
    print(i ** p, end=' ')
    i += 1

print("/Последнее число," "возведённое в степень:", i - 1 )

#3
prices = {
    'kievstar': 1.5,
    'tele2': 1.7,
    'vodafone': 1.9,
    'beeline': 1.3,
}


def main():
    operator = int(input('0. Киевстар\n1. Теле2\n2. Vodafone\n3. Beeline\nВыберите оператора (0-3): '))
    if operator < 0 or operator > 3:
        print('Неверный оператор')
        return
    duration = int(input('Введите длительность звонка (в минутах): '))
    print('Стоимость звонка: {} руб.'.format(prices[list(prices.keys())[operator]] * duration))


if __name__ == '__main__':
    main()

#4
a=int(input('Введите продажи 1 менеджера:'))
b=int(input('ВВедите продажи 2 менеджера:'))
c=int(input('ВВедите продажи 3 менеджера:'))

oklad = 200

if a>1000:
    zp1 = oklad+a*0.08
else:
    if a<500:
        zp1=oklad+a*0.03
    else:
        zp1=oklad+a*0.05
if b>1000:
    zp2=oklad+b*0.08
else:
    if b<500:
        zp2=oklad+b*0.03
    else:
        zp2=oklad+b*0.05
if c >1000:
    zp3=oklad+c*0.08
else:
    if c <500:
        zp3= oklad + c * 0.03
    else:
        zp3=oklad+c*0.05

if zp1>zp2 and zp1>zp3:
    print('Лучший по продажам - 2 менеджер!')
    zp1 += 200
if zp2 > zp1 and zp2 > zp3:
    print('Лучший по продажам - 2 менеджер!')
    zp2 += 200
if zp3 > zp1 and zp3 > zp2:
    print('Лучший по продажам - 3 менеджер!')
    zp3 += 200
print('Зарплата 1 менеджера ',zp1)
print('Зарплата 2 менеджера ',zp2)
print('Зарплата 3 менеджера ',zp3)


