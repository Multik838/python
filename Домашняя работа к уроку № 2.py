# Задание № 1

my_list = list('Набор букв')
my_list.append('Новая буква')
my_list.remove('Новая буква')
print(type(my_list))
print(my_list)

# Задание № 2

value_list = list(input("Введите значение: "))
j = 0
for i in range(int(len(value_list) // 2)):
    value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]
    j += 2

print(value_list)

#Задание № 3

my_value = input("Введите строку из нескольких слов, кол-во букв в слове не должно превышать 10: ")
my_words = []
num = 1
for el in range(my_value.count(' ') + 1):
    my_words = my_value.split()
    if len(str(my_words)) <= 10:
        print(f" {num} {my_words [el]}")
        num += 1
    else:
        print(f" {num} {my_words [el] [0:10]}")
        num += 1

#Задание № 4

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

#Задание № 5

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))









