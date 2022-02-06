# Дано нечетное натуральное число nn.
# Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:

# *
# **
# ***
# ****
# ***
# **
# *

# На вход программе подается одно нечетное натуральное число.

n = int(input())

for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(k):
        print('*', end='')
    print()