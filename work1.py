#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

number = int(input())
summ=0
summ += number // 100
summ += number % 100 // 10
summ += number % 10
print(summ)