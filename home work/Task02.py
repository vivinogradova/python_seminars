# # Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число: '))
firstDigit = n // 100
print(firstDigit)
secondDigit = (n % 100) // 10
print(secondDigit)
thirdDigit = n % 10
print(thirdDigit)

res = (n // 100) + ((n % 100) // 10) + (n % 10)
print(res)
