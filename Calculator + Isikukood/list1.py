# spisok=[]
# numbers=[1,2,3,4,5]
# abc=['Abc','B','C']
# slovo="Programmerimine"
# slovo_list=list(slovo)
# print(slovo)
# print(slovo_list)
# while True:
#     print('1 - Add new letter to list')
#     print('2 - extend list\n3-add letter om i- position')
#     print('4 - delete element')
#     valik=int(input())
#     if valik==1:
#         a=input('Enter letter')
#         slovo_list.append(a)
#         print(f'You added {a} new list',slovo_list)
#     elif valik==2:
#         slovo_list.extend(abc)
#         print(slovo_list)
#     elif valik==3:
#         a=input('Enter letter, which do you want add')
#         i=int(input('Enter number of possition'))
#         slovo_list.insert(i-1,a)
#         print(slovo_list)
#     elif valik==4:
#         a=input('Enter letter, which do you want delete')
#         n=slovo_list.count(a)
#         if n > 0:
#             for i in range(n):
#                 slovo_list.remove(a)
#         else:
#             print("We don't have that letter")
#         print(slovo_list)
# 1 Конкотенация (сложение строк)
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = list1 + list2
print(list1, list2, list3)
# 2 Повторение строки
print(list1 * 2)
# 3 Обращение по индексу
print(list1[1])
# 4 Извлечение среза
print(list2[:3])
# 5 Преведение строки к верхнему регистру под индексом 1
print(list2[1].upper())
# 6 Проверяет начинается ли солова или с большой буквы
print(list2[1].istitle())
# 7 Показывает состоит строка из str
print(list2[1].isalnum)
# 8 Показывает состоит ли строка из нижнего регистра
print(list2[4].islower())
# 9 Переводит символы нижнего регистра в верхний, а верхнего – в нижний
print(list2[3])
print(list2[3].swapcase())
#10  Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
list4 = ['Alooo', 'HELLO', 'pOKA']
print(list4[2])
print(list4[2].title())
