#Строки и переменные
str1 = "Я_не_готов_к_тому,_что_сейчас_произойдёт"

str2 = "Меня зовут Имя Фамилия Отчество"

str3 = "Тут пусто)"

str4 = ""

print("String Length =", len(str1))
#Метод len() - считает коллличество сиыолов в строке.

#Индексы строки:
        #print(str1[1])
        #print(str2[7])
        #print(str3[4])
a = str1[0]+" "+str1[2]+str1[3]+" "+str1[0]
print(a)

#str*[*:*] - диапозон строки(от:до)
print(str1[19:40] + "?")

print(str1[0:40:2])
print(str3[7:44:3])

print(str1.replace("_"," "))

print(str1[10:35].replace("_"," ",5))

#.split() - переводит в лист
print(str1.split("_"))

print(str1.lower())#все в нижний регистр
print(str1.upper())#все символы в ВЕРХНИЙ регистр
print(str1.title())#Первая Буква Станет Большой
print(str1.swapcase())# инвертирует регистр (большие станут маленькими, маленькие большими)

#i = "Я"
#q = "знаю"
#w = "python"
#print(i +" "+ q + " " +w)


#print("Ваша строка", input("ввелите сообщ "))
#a = input("ввелите сообщ ")
#print("Ваша строка", a)

#\n- перенос стороки
#\\
#\'
#\t
print("\'")

# \n print("test \n test2") рез: в разных строках
# \t print("test \t test2") рез: test test2
# \\ print("test \\ test2") рез: test \ test2
# \' print("test \' test2") рез: test ' test2
# \'' print("test \'' test2") рез: test '' test2

my_string = input()
my_string = my_string [2:6]+my_string[0]+my_string[9]+my_string[6:801]+my_string[1]+my_string[8]
print(my_string)

# зададим граф, как наборы вершин и смежных с ними вершин
# ACG – вершина A и смежные с ней C и G
b_str = 'ACG BDC CABDEFG DBCE ECDF FCEG GACF'
# зададим таблицу аналогичным способом
# 217 – пункт 2 и смежные с ним 1 и 7
d_str = '1234567 217 3157 4156 5134 614 7123'
# записываем информацию о графе в словарь
# вершина: смежные вершины
b_graph = {w[0]: set(w[1:]) for w in b_str.split()}
from itertools import permutations
# определяем все вершины
letters = 'ABCDEFG'
print(letters)
# перебираем все перестановки номеров
for perm in permutations('1234567'):
    # преобразуем цифровое представление в буквенное
        new_dstr = d_str
    # заменяя цифры на буквы (первую на 1, вторую на 2 ...)
    for old_d, new_b in zip(perm, letters):
        new_dstr = new_dstr.replace(old_d, new_b)
 # формируем словарь для измененной строки
    new_graph = {w[0]: set(w[1:])
            for w in new_dstr.split()}
 # если совпадает с начальным словарем с буквами
 if new_graph == b_graph:
 # выводим перестановку
    print(''.join(perm))
