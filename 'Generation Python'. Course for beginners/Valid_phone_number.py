# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером если она имеет формат:

# abc-def-hijk или
# 7-abc-def-hijk

# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

# Программа должна вывести «YES» если строка является корректным телефонным номером и «NO» в противном случае.

n = input().split("-")

if ''.join(n).isdigit():
    if n[0] == '7':
        del (n[0])
    if len(n[0]) == 3 and len(n[1]) == 3 and len(n[2]) == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
