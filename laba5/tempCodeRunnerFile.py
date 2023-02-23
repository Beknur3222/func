san = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        san.append(n)
san.sort(reverse=False)
print('--------------------------------')
for i in san:
            print(i, end=' \n')  