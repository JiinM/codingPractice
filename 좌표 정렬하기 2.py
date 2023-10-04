n = int(input())
list = []

for i in range(n):
    a, b = input().split()
    list.append([int(b), int(a)])

list.sort()
ans = []
for i in range(0, len(list)):
    ans.append([list[i][1], list[i][0]])

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
