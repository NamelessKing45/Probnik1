# # зададим граф, как наборы вершин и смежных с ними вершин
# # ACG – вершина A и смежные с ней C и G
# b_str = 'ACG BDC CABDEFG DBCE ECDF FCEG GACF'
# # зададим таблицу аналогичным способом
# # 217 – пункт 2 и смежные с ним 1 и 7
# d_str = '1234567 217 3157 4156 5134 614 7123'
# # записываем информацию о графе в словарь
# # вершина: смежные вершины
# b_graph = {w[0]: set(w[1:]) for w in b_str.split()}
# from itertools import permutations
# # определяем все вершины
# letters = 'ABCDEFG'
# print(letters)
# # перебираем все перестановки номеров
# for perm in permutations('1234567'):
#     new_dstr = d_str
#     for old_d, new_b in zip(perm, letters):
#         new_dstr = new_dstr.replace(old_d, new_b)
#         new_graph = {w[0]: set(w[1:])
#                      for w in new_dstr.split()}
#         if new_graph == b_graph:
#             print(''.join(perm))
#Задача 1
# str_1 = "Я"
# str_2 = "знаю"
# str_3 = "Python"
# print(str_1,str_2,str_3)
#Задача 2
# Per = input("Введите строку\t")
# print('"Ваша строка-"'+Per+".")
#Задача 3
# str2 = ("Я.внима?тельноне_слушал учителя.и?не_понял.всё!!!")
# a = str2.replace("_"," ").replace(".", " ").replace("?","").replace("!!!","!").replace("!!!","!").replace("ине","и не")
# print(a)
#Задача 4
# str3 = input("Введите фамилию, имя, отчество. ")
# print(str3.lower().title())
#Задача 5
# str1 = "Я не могу решить эту сложную задачу"
# print(str1.replace("не","").replace("  "," "))
# a = str1.split()
# print(a[6].replace("у","а").replace("з","З"), a[1], a[5].replace("ую","ая"))