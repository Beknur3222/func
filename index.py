# print("ozgeriz")
# # print("Hello world!")
# # print("Hello Git")
# print("Laba")
# print("help me")
#1
# a = int(input('A = '))
# b = int(input('B = '))
# if a<=b:
#     for i in range(b-a+1):
#         i+=a
#         print(i)
# else:
#     print('ERROR')
#2
# a = int(input('A = '))
# b = int(input('B = '))
# if a<b:
#     for i in range(b-a+1):
#         i+=a
#         print(i)
# else:
#     for i in range(a-b+1):
#         i-=a
#         i*=-1
#         print(i)
#3
# a = int(input('A = '))
# b = int(input('B = '))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')
#4
# import random
# n = int(input('N = '))
# x = random.randrange(n)
# a=1
# sum1=0
# sum=0
# for i in range(n-a+1):
#     if i==x:
#         continue
#     sum+=i
#     i+=1
# for i in range(n-a+1):
#     sum1+=i
#     i+=1
# print(x)
# print(sum1-sum )

# git init 
# git add main.py README.md
# git commit -m "first project"
# git log
# git remote
# git push 


#-----------------------------------------------------------------------------------------------------------------------------------
#laba1
# z = input('Ваша фамилия, имя? ')
# x = input('Сколько Вам лет? ')
# c = input('Где вы живете? ')
# print('Ваши фамилия, имя', z)
# print('Ваш возраст', x)
# print('Вы живете в', c)
#laba2
# import math
# x = int(input('x = '))
# t = int(input('t = '))
# z = (9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t)))*math.pow(math.e,x)
# print("z = {0:.2f}".format(z))
#laba3
# z = int(input('Введите целое число: '))
# x = int(input('Введите целое число: '))
# c = int(input('Введите целое число: '))
# if z>=1 and z<=3:
#     print('В интервал [1,3] входит ', z)
# else:
#     print(z, 'Не входит в интервал [1,3]')
# if x>=1 and x<=3:
#     print('В интервал [1,3] входит ', x)
# else:
#     print(x, 'Не входит в интервал [1,3]')
# if c>=1 and c<=3:
#     print('В интервал [1,3] входит ', c)
# else:
#     print(c, 'Не входит в интервал [1,3]')
#laba4-1
# z = int(input('Введите вещественное число: '))
# for i in range(10):
#     i=i+1
#     print('Цена', i, 'кг конфет ровна', z*i,'тг')
#laba4-2
# i = int(input('Введите число: '))
# sum=1
# kol=0
# while i!=0:
#     sum+=i
#     kol+=1
#     print(i, end=' ')
#     i-=1
# print('\n')
# print('Сумма:', sum)
# print('Количество: ', kol)






















# #9
# #Определить, сколько раз в тексте встречается заданное слово.
# t = str(input('Введите текст: ')).split()
# s = str(input('Введите слово: '))
# x = 0
# for i in t:
#     if i == s:
#         x += 1
# print('Количества', s, 'в тексте:', x)














#laba1
# z = input('Ваша фамилия, имя? ')
# x = input('Сколько Вам лет? ')
# c = input('Где вы живете? ')
# print('Ваши фамилия, имя ', z)
# print('Ваш возраст ', x)
# print('Вы живете в ', c)
#laba2
# import math
# x = int(input('x = '))
# t = int(input('t = '))
# z = (9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t)))*math.pow(math.e,x)
# print("z = {0:.2f}".format(z))
#laba3
# z = int(input('Введите целое число: '))
# x = int(input('Введите целое число: '))
# c = int(input('Введите целое число: '))
# if z>=1 and z<=3:
#     print('В интервал [1,3] входит ', z)
# else:
#     print(z, 'Не входит в интервал [1,3]')
# if x>=1 and x<=3:
#     print('В интервал [1,3] входит ', x)
# else:
#     print(x, 'Не входит в интервал [1,3]')
# if c>=1 and c<=3:
#     print('В интервал [1,3] входит ', c)
# else:
#     print(c, 'Не входит в интервал [1,3]')
#laba4-1
# z = int(input('Введите вещественное число: '))
# for i in range(10):
#     i=i+1
#     print('Цена', i, 'кг конфет ровна', z*i,'тг')
#laba4-2
# i = int(input('Введите число: '))
# sum=1
# kol=0
# while i!=0:
#     sum+=i
#     kol+=1
#     print(i, end=' ')
#     i-=1
# print('\n')
# print('Сумма:', sum)
# print('Количество: ', kol)
























#9
#Определить, сколько раз в тексте встречается заданное слово.
# t = input('Введите текст: ')
# s = input('Введите слово: ')
# flag = 0
# n = 0
# string = ''
# print('t.find(s) = ', t.find(s))
# # for i in range(len(t)):
#         # if True:
#         #     flag = t.find(s, flag, flag+len(s))
#         #     n=n+1
# i=len(t)
# while i!=0:
#     if " "+s+" " in (" " + t + " "):
#         n+=1
#
# print(flag)
# print(n)

# my_string = "Добро пожаловать"
# start = -1
# count = 0
#
# while True:
#     start = my_string.find("о", start+1)
#     if start == -1:
#         break
#     count += 1
#
# print("Количество вхождений символа в строку: ", count )