#1esep
# import random
# def kor():
#     kor1 = tuple(random.randint(0, 5) for _ in range(10))
#     kor2 = tuple(random.randint(-5, 0) for _ in range(10))
#     return kor1, kor2
# kor1, kor2 = kor()
# kor3 = kor1 + kor2
# sum = kor3.count(0)
# print("Kor1: ", kor1)
# print("Kor2: ", kor2)
# print("Kor3: ", kor3)
# print("Sum:", sum)

#2esep
# matryoshka = (35, (3.14, (6+2j, ('beknur', ()))))
# print(matryoshka)
# tuple1 = matryoshka[0]
# tuple2 = matryoshka[1][0]
# tuple3 = matryoshka[1][1][0]
# tuple4 = matryoshka[1][1][1][0]
# tuple5 = matryoshka[1][1][1][1]
# print("tuple1:", tuple1)
# print("tuple2:", tuple2)
# print("tuple3:", tuple3)
# print("tuple4:", tuple4)
# print("tuple5:", tuple5)

#3esep
# import random
# Categorias = ('car', 'dinner', 'other')
# Days = ('duisenbi', 'sarsenbi', 'seisenbi', 'beisenbi', 'juma', 'senbi', 'jeksenbi')
# Wygyndar = {}
# for day in Days:
#     Wygyndar[day] = []
#     for x in Categorias:
#             #wygyn = float(input(f'{day} kuni "{x}"  : '))
#             wygyn = float(random.randint(1, 9) * 100)
#             print(f'{day} kuni "{x}"  : {wygyn}')
            
#             Wygyndar[day].append(wygyn)
# sum_wygyn = 0
# for day in Wygyndar:
#     sum_wygyn += sum(Wygyndar[day])
# print('Wygyn all days:')
# for day in Wygyndar:
#     print(f'{day}: {Wygyndar[day]}')
# print(f'Sum: {sum_wygyn}')

#4esep
# x = input("Students name: ")
# names = x.split()
# names_kor = tuple(names)
# print("'jan' in name: ", end="")
# for name in names_kor:
#     if "jan" in name:
#         print(name, end=" ")
# print('')

#5esep
# cyr = ('а','ә','б','в','г','ғ','д','е','ё','ж','з','и','й','к','қ','л','м','н','ң','о','ө','п','р','с','т','у','ұ','ү','ф', 'х', 'һ','ц','ч','ш','щ','ъ','ы','і','ь','э','ю','я')
# lat = ('a','a','b','v','g','g','d','e','io','j','z','i','i','k','q','l','m','n','n','o','o','p','r','s','t','u','u','u','f','h','h','ts','ch','sh','shch','','y','i','','e','iu','ia')
# soz = input("Soz: ")
# for i in soz:
#     n = 0
#     for j in cyr:
#         if j == i:
#             print(lat[n],end="")
#             break
#         elif i.lower() == j:
#             print(lat[n].upper(),end="")
#             break
#         n +=1
# print('')





















# cyr = ('а','ә','б','в','г','ғ','д','е','ё','ж','з','и','й','к','қ','л','м','н','ң','о','ө','п','р','с','т','у','ұ','ү','ф', 'х', 'һ','ц','ч','ш','щ','ъ','ы','і','ь','э','ю','я')
# lat = ('a','a','b','v','g','g','d','e','io','j','z','i','i','k','q','l','m','n','n','o','o','p','r','s','t','u','u','u','f','h','h','ts','ch','sh','shch','','y','i','','e','iu','ia')
# soz = input("\nSoz: ")
# for i in soz:
#     san = 0
#     for j in cyr:
#         if j == i:
#             print(lat[san],end="")
#             break
#         elif i.lower() == j:
#             print(lat[san].upper(),end="")
#             break
#         san +=1
# print('')


# from transliterate import translit
# kaz_arip = ('ә', 'і', 'ң', 'ғ', 'ү', 'ұ', 'қ', 'ө', 'һ')
# lat_arip = ('a', 'y', 'n', 'g', 'u', 'u', 'q', 'o', 'h')
# soz = input("\nSoz: ")
# lat = translit(soz, language_code='ru', reversed=True)
# qwe = list(lat)
# # print(qwe)
# for i in qwe:
#     san = 0
#     for j in kaz_arip:
#         if j != i:
#             print(i, end='')
#             break
#         else:
#             print(lat_arip[san], end='')
#             break
#         san += 1
# print('')

# for i in lat:
#     san = 0
#     for j in kaz_arip:
#         if j == i:
#             lat[i] = lat_arip[san]
#             print(str(lat[i]), end="")
#             break
#         san += 1


