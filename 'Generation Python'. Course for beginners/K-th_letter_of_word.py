# На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
ls1 = []
for i in range(n):
    ls1.append(input())

k = int(input())
for i in range(n):
    print(ls1[i][k - 1:k], end="")
