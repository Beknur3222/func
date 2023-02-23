#laba5-1
# students = []
# sc = []
# while True:
#     print(' 1-Student input;\n 2-View student list;\n 3-View sort student list #name;\n 4-View sort student list #course;\n 0-exit;\n')
#     cmd = int(input())
#     sc = []
#     if cmd == 1:
#         student=input('Name: ')
#         course=input('Course: ')
#         sc.append(student)
#         sc.append(course)
#         students.append(sc)
#     elif cmd == 2:
#         print('Name and Course')
#         for student in students:
#              print(student)
#              print("------")
#     elif cmd == 3:
#         print('Name and Course')
#         sortL = students
#         sortL.sort()
#         for student in sortL:
#             print(student)
#             print("------")
#     elif cmd == 4:
#         print('Name and Course')
#         sortQ = students
#         sortQ.sort(key = lambda x: x[1])
#         for student in sortQ:
#             print(student)
#             print("------")
#     elif cmd == 0:
#         break
#     else:
#         continue

#laba5-2
# import pandas as pd
# df = pd.DataFrame([[100, 90, 80], [75, 85, 95], [70, 100, 80]],
#         index = ['fiz', 'math', 'Eng'],
#         columns = ['Beknur', 'Daryn', 'Bagdat'])
# # students = [['Beknur', ], [], [], [], []]
# while True:
#     print(df)
#     n = input()
#     if n == 'Beknur':
#         result_two = df.loc[:, n]
#         print(result_two)
#     elif n == 'Daryn':
#         result_two = df.loc[:, n]
#         print(result_two)
#     elif n == 'Bagdat':
#         result_two = df.loc[:, n]
#         print(result_two)
#     elif n == 'q':
#         break
#     else:
#         continue

#laba5-3
# san = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         san.append(n)
# san.sort(reverse=False)
# print('--------------------------------')
# for i in san:
#             print(i, end=' \n')  

#laba5-4
# san = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         san.append(n)
# san.sort(reverse=True)
# print('--------------------------------')
# for i in san:
#             print(i, end=' \n') 

#laba5-5
# import random
# ticket = []
# while True:
#     n = int(random.randint(1, 49))
#     if n != ticket:
#         ticket.append(n)
#     else:
#         continue
#     if len(ticket)==6:
#         break
# ticket.sort()
# print(ticket)


#laba5-6
# lis = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         lis.append(n)
# a = sorted(lis, reverse=True)
# b = sorted(lis, reverse=False)
# if a == lis or b == lis:
#     print(True)
# else:
#     print(False)