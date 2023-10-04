n = int(input())
list = []

for i in range(n):
    a, b = input().split()
    list.append([int(a), int(b)])

list.sort()

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()
