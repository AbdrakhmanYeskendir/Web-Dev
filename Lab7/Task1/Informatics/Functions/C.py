def xor(a, b):
    if a != b:
        return 1
    else:
        return 0

line = input().split()
a = int(line[0])
b = int(line[1])

print(xor(a, b))
