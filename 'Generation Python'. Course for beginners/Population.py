# На вход программе подается три натуральных числа m, p, n:
#
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
#
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая n-м днем.


a, b, c = [int(input()) for i in range(3)]

for i in range(1, c + 1):
    print(i, a)
    a += a * b / 100
