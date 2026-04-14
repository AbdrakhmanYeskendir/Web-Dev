n = int(input())

i = 1
while i <= n:
    root = int(i ** 0.5)
    if root * root == i:
        print(i)
    i += 1