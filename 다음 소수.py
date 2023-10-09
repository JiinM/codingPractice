import sys

input = sys.stdin.readline
n = int(input())


def ch(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for _ in range(n):
    i = int(input())
    while True:
        if i == 0 or i == 1:
            print(2)
            break
        if ch(i):
            print(i)
            break
        else:
            i += 1
