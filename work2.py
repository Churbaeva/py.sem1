#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
 #чем Петя и Сережа вместе?#
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#   60 -> 10  40  10

summ=0
number = int(input('Количество журавликов: ' ))
print(int(number / 6), int(number * 2 / 3), int(number / 6))
