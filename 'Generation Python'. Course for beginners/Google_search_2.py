# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

# Примечание. Поиск не должен быть чувствителен к регистру символов.

ls1 = [input() for i in range(int(input()))]
ls2 = [input() for i in range(int(input()))]

for i in ls1:
    for j in ls2:
        if j.lower() not in i.lower():
            break
    else:
        print(i)
