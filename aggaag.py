# Урок №6. Циклы while и for
# Задание №1
# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество


#Я особо не понял задание поэтому за равное нулю подозреваю целое число
N=int(input())
count=0
while N-1>=0:
    N1=int(input())
    N -= 1
    if N1%2==0:
        count+=1
        print(count)
#Или вот втрое решение с равенством нулю
N=int(input())
count=0
while N-1>=0:
    N1=int(input())
    N -= 1
    if N1==0:
        count+=1
        print(count)
# Задание №2
# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)
chislo1=int(input())
for i in range(1,2000000):
    if chislo1%i==0:
        print(i)
# Задание №3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.
chis_1,chis_2=map(int,input().split())
if chis_1%2==0 and chis_2%2==0:
    if chis_1 <= chis_2:
        for i in range(chis_1,chis_2,2):
            print(i)






